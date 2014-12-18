import copy
import random

from core.buckets import BucketOrder, BucketOrderInfo, BucketExtend
from core.camera import Camera
from core.intersection import Intersection
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.scene import Scene
from core.parallel import ThreadPool
from core.sampler import Sampler


class BoundingVolumeRenderer(Renderer):
    def __init__(self, sampler: Sampler, camera: Camera):
        super().__init__()

        self.scene = None
        self.camera = camera
        self.main_sampler = sampler

    def draw_bucket_extend(self, bucket_extend: BucketExtend):
        pass
        for x in range(bucket_extend.start_x, bucket_extend.end_x):
            self.camera.film.data[bucket_extend.start_y, x] = 0xffffffff
            self.camera.film.data[bucket_extend.end_y - 1, x] = 0xffffffff

        for y in range(bucket_extend.start_y, bucket_extend.end_y):
            self.camera.film.data[y, bucket_extend.start_x] = 0xffffffff
            self.camera.film.data[y, bucket_extend.end_x - 1] = 0xffffffff

    def render_task(self, task_index: int,
                    bucket_index: int,
                    bucket_order_info: BucketOrderInfo, sample, renderer):

        sampler = self.main_sampler.get_sub_sampler(bucket_index, bucket_order_info)

        if sampler is None:
            return

            # print("start render task : id(" + str(task_index) + ") (" + str(sampler.bucket_extend.start_x) + "," + str(
            #           sampler.bucket_extend.start_y) + ") " + "(" + str(sampler.bucket_extend.end_x - 1) + "," + str(
            #          sampler.bucket_extend.end_y - 1) + ")")

        self.draw_bucket_extend(sampler.bucket_extend)

        max_samples_count = self.main_sampler.get_maximum_sample_count()

        rays = [Ray] * max_samples_count

        while True:

            samples = []
            sampler.get_more_samples(samples)

            if len(samples) == 0:
                break

            intersection = Intersection()

            for i in range(len(samples)):
                x = int(samples[i].image_xy[0])
                y = int(samples[i].image_xy[1])

#                rays[i] = self.camera.generate_ray(new_samples_list[i], rays[i])

                self.camera.film.data[y, x] = self.get_li(self.scene, rays[i], intersection)


                # print("end render task " + str(task_index))

    def get_li(self, scene, ray: Ray, intersection: Intersection, sample: Sample)->Spectrum:
        color = 0xff303030
        if self.scene.get_intersection(ray, intersection):
            color = min(intersection.ray_epsilon / 5.0 * 100, 255)
        else:
            color = 0xff303030
        return color

    def render(self, scene, bucket_order_info: BucketOrderInfo, multiThread: bool=True):

        self.scene = scene

        sample_list = [Sample(self.main_sampler, scene)]

        my_bucket_orders = BucketOrder.create(bucket_order_info.width, bucket_order_info.height,
                                              bucket_order_info.bucket_order_type)

        # 1) Init a Thread pool with the desired number of threads
        pool = ThreadPool(1)

        # 2) Add the task to the queue
        task_index = 0
        for i in range(bucket_order_info.width * bucket_order_info.height):
            pool.add_task(self.render_task,
                          task_index,
                          my_bucket_orders.buckets_orders[task_index],
                          bucket_order_info,
                          sample_list,
                          random.random() * 255)
            task_index += 1

        # 3) Wait for completion
        pool.wait_completion()
