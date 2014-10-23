import copy
import multiprocessing
from multiprocessing.dummy import Manager
from multiprocessing.pool import Pool
import os
import random

from core.buckets import BucketOrder, BucketOrderInfo, BucketExtend
from core.camera import Camera
from core.intersection import Intersection
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.scene import Scene
from core.sampler import Sampler
from core.spectrum import Spectrum
from maths.config import infinity_max_f
from shapes.plane import Plane
from shapes.sphere import Sphere


def write_png(buf, width, height):
    """ buf: must be bytes or a bytearray in py3, a regular string in py2. formatted RGBARGBA. """
    import zlib, struct

    # reverse the vertical line order and add null bytes at the start
    width_byte_4 = width * 4
    raw_data = b''.join(b'\x00' + buf[span:span + width_byte_4]
                        for span in range((height - 1) * width * 4, -1, - width_byte_4))

    def png_pack(png_tag, data):
        chunk_head = png_tag + data
        return (struct.pack("!I", len(data)) +
                chunk_head +
                struct.pack("!I", 0xFFFFFFFF & zlib.crc32(chunk_head)))

    return b''.join([
        b'\x89PNG\r\n\x1a\n',
        png_pack(b'IHDR', struct.pack("!2I5B", width, height, 8, 6, 0, 0, 0)),
        png_pack(b'IDAT', zlib.compress(raw_data, 9)),
        png_pack(b'IEND', b'')])


def saveAsPNG(array, filename):
    import struct

    if any([len(row) != len(array[0]) for row in array]):
        raise ValueError("Array should have elements of equal size")

        # First row becomes top row of image.
    flat = []
    map(flat.extend, reversed(array))
    # Big-endian, unsigned 32-byte integer.
    buf = b''.join([struct.pack('>I', ((0xffFFff & i32) << 8) | (i32 >> 24))
                    for i32 in flat])  # Rotate from ARGB to RGBA.

    data = write_png(buf, len(array[0]), len(array))
    f = open(filename, 'wb')
    f.write(data)
    f.close()


class AmbientOcclusionRenderer(Renderer):

    def __init__(self, sampler: Sampler, camera: Camera, samples_count: int=1, max_distance: float=infinity_max_f):
        super().__init__()

        self.camera = camera
        self.main_sampler = sampler
        self.samples_count = samples_count
        self.max_distance = max_distance

    def draw_bucket_extend(self, bucket_extend: BucketExtend):
        for x in range(bucket_extend.start_x, bucket_extend.end_x):
            self.camera.film.data[bucket_extend.start_y, x] = 0xffffffff
            self.camera.film.data[bucket_extend.end_y - 1, x] = 0xffffffff

        for y in range(bucket_extend.start_y, bucket_extend.end_y):
            self.camera.film.data[y, bucket_extend.start_x] = 0xffffffff
            self.camera.film.data[y, bucket_extend.end_x - 1] = 0xffffffff

    def render_task(self, task_index: int,
                    bucket_index: int,
                    bucket_order_info: BucketOrderInfo,
                    color: int):

        sampler = self.main_sampler.get_sub_sampler(bucket_index, bucket_order_info)

        if sampler == None:
            return

        print("start render task : id(" + str(task_index) + ") (" + str(sampler.bucket_extend.start_x) + "," + str(
            sampler.bucket_extend.start_y) + ") " + "(" + str(sampler.bucket_extend.end_x - 1) + "," + str(
            sampler.bucket_extend.end_y - 1) + ")")

        self.draw_bucket_extend(sampler.bucket_extend)

        pixels = []

        while True:

            samples = sampler.get_more_samples()

            if len(samples) == 0:
                break

            intersection = Intersection()

            spectrum = Spectrum(0.0)
            spectrum_count = 0

            for i in range(len(samples)):
                ray = self.camera.generate_ray(samples[i])

                # if self.scene.get_is_intersected(rays[i]):
                if self.scene.get_intersection(ray, intersection):
#                    if type(intersection.differentialGeometry.shape) == Sphere:
#                        spectrum.components[0] = 1.0
#                        spectrum.components[1] = 0.0
#                        spectrum.components[2] = 0.0
#                    else:
                    spectrum += self.scene.surface_integrator.Li(self.scene, ray, intersection)

                spectrum_count += 1
            pixels.append(spectrum / float(spectrum_count))

        print("end render task " + str(task_index))

        return pixels, sampler.bucket_extend

    def draw(self, args):
        pixels = args[0]
        bucket_extend = args[1]
        i = 0
        for y in range(bucket_extend.start_y, bucket_extend.end_y, 1):
            for x in range(bucket_extend.start_x, bucket_extend.end_x, 1):
                r, g, b = pixels[i].toRGB()
                self.camera.film.data[y, x] = int(r * 255.0) | int(g * 255.0) << 8 | int(g * 255.0) << 16
                i += 1


    def render(self, scene: Scene, bucket_order_info: BucketOrderInfo):

        self.scene = scene

        my_bucket_orders = BucketOrder.create(bucket_order_info.width, bucket_order_info.height,
                                              bucket_order_info.bucket_order_type)

        pool = Pool(processes=multiprocessing.cpu_count())

        results = []

        for i in range(bucket_order_info.width * bucket_order_info.height):
            a = pool.apply_async(self.render_task, args=(
                i, my_bucket_orders.buckets_orders[i], bucket_order_info, random.random() * 255),
                                 callback=self.draw)
            results.append(a)

        for r in results:
            r.wait()

        print("Render end")

        data = write_png(self.camera.film.data, self.camera.film.width, self.camera.film.height)
        with open("my_image.png", 'wb') as fd:
            fd.write(data)

