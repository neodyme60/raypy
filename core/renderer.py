from core.buckets import BucketOrderSortType, BucketOrderInfo
from core.intersection import Intersection
from core.ray import Ray
from core.sample import Sample

class Renderer:

    def __init__(self):
        pass

    def render(self, scene, bucket_order_info: BucketOrderInfo):
        raise NotImplementedError

    def render_task(self, task_index: int, bucket_index: int, bucket_order_info: BucketOrderInfo, sample: Sample, color: int):
        raise NotImplementedError

    def get_li(self, scene, ray: Ray, intersection: Intersection):
        pass