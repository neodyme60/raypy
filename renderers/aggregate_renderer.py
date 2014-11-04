from core.buckets import BucketOrderSortType, BucketOrderInfo
from core.intersection import Intersection
from core.renderer import Renderer
from core.sample import Sample
from core.scene import Scene


class AggregateRendererTask(Renderer):
    def __init__(self):
        super().__init__()

class AggregateRenderer(Renderer):

    def __init__(self, scene:Scene):
        super().__init__()

    def render_task(self, task_index: int, bucket_index: int, bucket_order_info: BucketOrderInfo, color: int):
        pass

    def render(self, scene, bucket_order_info: BucketOrderInfo, multiThread: bool=True):
        pass

    def get_li(self, scene: Scene, sample: Sample, intersection: Intersection):
        pass