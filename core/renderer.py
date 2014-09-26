from core.buckets import BucketOrderSortType, BucketOrderInfo
from core.sample import Sample
from core.scene import Scene

class Renderer:

    def __init__(self):
        pass

    def render(self, scene: Scene, bucket_order_info: BucketOrderInfo):
        raise NotImplementedError

    def render_task(self, task_index: int, bucket_index: int, bucket_order_info: BucketOrderInfo, sample: Sample, color: int):
        raise NotImplementedError

    def Li(self):
        pass
