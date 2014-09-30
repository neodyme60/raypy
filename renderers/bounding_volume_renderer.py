import copy
import random

from core.buckets import BucketOrder, BucketOrderInfo, BucketExtend
from core.camera import Camera
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.scene import Scene
from core.parallel import ThreadPool
from core.sampler import Sampler


class BoundingVolumeRenderer(Renderer):
    def __init__(self, sampler: Sampler, camera: Camera):
        Renderer.__init__(self)

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
                    bucket_order_info: BucketOrderInfo,
                    sample_list: Sample,
                    color: int):

        sampler = self.main_sampler.get_sub_sampler(bucket_index, bucket_order_info)

        if sampler == None:
            return

#        print("start render task : id(" + str(task_index) + ") (" + str(sampler.bucket_extend.start_x) + "," + str(
 #           sampler.bucket_extend.start_y) + ") " + "(" + str(sampler.bucket_extend.end_x - 1) + "," + str(
  #          sampler.bucket_extend.end_y - 1) + ")")

        self.draw_bucket_extend(sampler.bucket_extend)

        max_samples_count = self.main_sampler.get_maximum_sample_count()

        new_samples_list = copy.deepcopy(sample_list)

        rays = [Ray] * max_samples_count

        while True:
            sampleCount = sampler.get_more_samples(new_samples_list)

            if sampleCount == 0:
                break

            intersection = None

            for i in range(sampleCount):
                x = int(new_samples_list[i].image_xy[0])
                y = int(new_samples_list[i].image_xy[1])
                # self.camera.film.data[y, x] = (int(color) << 8)
                rays[i] = self.camera.generate_ray(new_samples_list[i], rays[i])
                has_intersection = self.scene.intersect(rays[i], intersection)
                if has_intersection == True:
                    self.camera.film.data[y, x] = 0xffffffff
                else:
                    self.camera.film.data[y, x] = 0xff0000ff

#        print("end render task " + str(task_index))


    def render(self, scene: Scene, bucket_order_info: BucketOrderInfo):

        self.scene = scene

        sample_list = []
        sample_list.append(Sample(self.main_sampler, scene))

        my_bucket_orders = BucketOrder.create(bucket_order_info.width, bucket_order_info.height,
                                              bucket_order_info.bucket_order_type)

        # 1) Init a Thread pool with the desired number of threads
        pool = ThreadPool(7)

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
