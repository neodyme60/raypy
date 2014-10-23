from core.buckets import BucketOrderInfo
from core.intersection import Intersection
from core.ray import Ray


class Renderer:
    def __init__(self):
        pass

    def render(self, scene, bucket_order_info: BucketOrderInfo):
        raise NotImplementedError

    def render_task(self, task_index: int,
                    bucket_index: int,
                    bucket_order_info: BucketOrderInfo,
                    color: int):
        raise NotImplementedError

    def get_li(self, scene, ray: Ray, intersection: Intersection):
        pass