import random

from core.buckets import BucketOrderSortType, BucketOrder, BucketOrderInfo
from core.camera import Camera
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

    def render_task(self, task_index: int, bucket_index: int, bucket_order_info: BucketOrderInfo, sample: Sample,
                    color: int):

        maxSamples = self.main_sampler.get_Maximum_Sample_Count()

        sampler = self.main_sampler.get_sub_sampler(bucket_index, bucket_order_info)

        print("start render task : id(" + str(task_index) + ") (" + str(sampler.pixel_start_x) + "," + str(
            sampler.pixel_start_y) + ") " + "(" + str(sampler.pixel_end_x) + "," + str(
            sampler.pixel_end_y) + ")")  # my_samples = sample.duplicate(maxSamples)

        for x in range(sampler.pixel_start_x, sampler.pixel_end_x):
            for y in range(sampler.pixel_start_y, sampler.pixel_end_y):
                self.camera.film.data[x][y] = (int(color) << 8)

        print("end render task " + str(task_index))


    def render(self, scene: Scene, bucket_order_info: BucketOrderInfo):
        my_sample = Sample(self.main_sampler, scene)

        my_bucket_orders = BucketOrder.create(bucket_order_info.width, bucket_order_info.height,
                                              bucket_order_info.bucket_order_type)

        # 1) Init a Thread pool with the desired number of threads
        pool = ThreadPool(1)

        # 2) Add the task to the queue
        task_index = 0
        for i in range(bucket_order_info.width * bucket_order_info.height):
            pool.add_task(self.render_task, task_index, my_bucket_orders.buckets_orders[task_index],
                          bucket_order_info, my_sample, random.random() * 255)
            task_index += 1

        # 3) Wait for completion
        pool.wait_completion()
