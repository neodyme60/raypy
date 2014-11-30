from copy import deepcopy
import multiprocessing
from multiprocessing.pool import Pool
import random
import itertools

from core.buckets import BucketOrder, BucketOrderSortType
from core.buckets import BucketOrderInfo
from core.buckets import BucketExtend

from core.camera import Camera
from core.intersection import Intersection
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.sampler import Sampler
from core.scene import Scene
from core.spectrum import Spectrum
from core.surface_integrator import SurfaceIntegrator
from core.volume_integrator import VolumeIntegrator
from maths.config import infinity_max_f
from maths.tools import get_clamp


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


class SamplerRenderer(Renderer):

    def __init__(self, sampler: Sampler, camera: Camera, surface_integrator: SurfaceIntegrator, volume_integrator: VolumeIntegrator):
        super().__init__()

        self.camera = camera
        self.main_sampler = sampler
        self.surface_integrator = surface_integrator
        self.volume_integrator = volume_integrator

    def draw_bucket_extend(self, bucket_extend: BucketExtend):
        for x in range(bucket_extend.start_x, bucket_extend.end_x):
            self.camera.film.data[bucket_extend.start_y, x] = 0xffffffff
            self.camera.film.data[bucket_extend.end_y - 1, x] = 0xffffffff

        for y in range(bucket_extend.start_y, bucket_extend.end_y):
            self.camera.film.data[y, bucket_extend.start_x] = 0xffffffff
            self.camera.film.data[y, bucket_extend.end_x - 1] = 0xffffffff

    def render_task(self, task_index: int,
                    bucket_index: int,
                    bucket_order_info: BucketOrderInfo, sample, renderer: Renderer):

        sampler = self.main_sampler.get_sub_sampler(bucket_index, bucket_order_info)

        if sampler == None:
            return

        print("start render task : id(" + str(task_index) + ") (" + str(sampler.bucket_extend.start_x) + "," + str(
            sampler.bucket_extend.start_y) + ") " + "(" + str(sampler.bucket_extend.end_x - 1) + "," + str(
            sampler.bucket_extend.end_y - 1) + ")")

        self.draw_bucket_extend(sampler.bucket_extend)

        pixels = []


        maxSamples = sampler.get_maximum_sample_count()
        samples = list(itertools.repeat(deepcopy(sample), maxSamples))

        #preallocate array for each pixels
        rays = [Ray()]*maxSamples
        Ls = [Spectrum(0.0)]*maxSamples
        Ts = [Spectrum(0.0)]*maxSamples
        intersections = [Intersection()]*maxSamples

        while True:

            if sampler.get_more_samples(samples) == 0:
                break

            for i in range(len(samples)):
                rays[i] = self.camera.generate_ray(samples[i])
                Ls[i] = renderer.get_li(self.scene, rays[i], intersections[i], samples[i])

            s = Spectrum(0.0)
            for i in range(len(samples)):
                s +=Ls[i]
            pixels.append(s / float(len(samples)))

        print("end render task " + str(task_index))

        return pixels, sampler.bucket_extend

    def get_li(self, scene, ray: Ray, intersection: Intersection, sample: Sample)->Spectrum:

        Li = Spectrum(0.0)
        if self.scene.get_intersection(ray, intersection):
            Li = self.surface_integrator.Li(scene, self, ray, intersection, sample)
        else:
            #Handle ray that doesn't intersect any geometry
            for l in scene.lights:
               Li += l.Le(ray)

        #todo transmitance

        return Li


    def draw(self, args):
        pixels = args[0]
        bucket_extend = args[1]
        i = 0
        for y in range(bucket_extend.start_y, bucket_extend.end_y, 1):
            for x in range(bucket_extend.start_x, bucket_extend.end_x, 1):
                r, g, b = pixels[i].toRGB()
                self.camera.film.data[y, x] = int(get_clamp(b,0.0, 1.0) * 255.0) | int(get_clamp(g,0.0, 1.0) * 255.0) << 8 | int(get_clamp(r,0.0, 1.0) * 255.0) << 16
                i += 1


    def render(self, scene, bucket_order_info: BucketOrderInfo, multiThread: bool=True):

        self.scene = scene

        sample = Sample(self.main_sampler, self.surface_integrator, self.volume_integrator, scene)

        if multiThread==True:
            my_bucket_orders = BucketOrder.create(bucket_order_info.width, bucket_order_info.height,
                                                  bucket_order_info.bucket_order_type)

            pool = Pool(processes=multiprocessing.cpu_count())
#            pool = Pool(processes=1)
            pool._wrap_exception = False

            results = []

            for i in range(bucket_order_info.width * bucket_order_info.height):
                a = pool.apply_async(self.render_task, args=(
                    i, my_bucket_orders.buckets_orders[i], bucket_order_info, sample, self),
                                     callback=self.draw)
                results.append(a)

            for r in results:
                r.wait()

        else:
            bucketOrderInfo = BucketOrderInfo(BucketOrderSortType.Random, 1, 1)
            self.render_task(0, 0, bucketOrderInfo, sample, 0, self)

        print("Render end")

        data = write_png(self.camera.film.data, self.camera.film.width, self.camera.film.height)
        with open("my_image.png", 'wb') as fd:
            fd.write(data)

    def Transmittance(self, scene: Scene, ray: Ray, sample: Sample)->Spectrum:
        return self.volume_integrator.Transmittance(scene, self, ray, sample)
