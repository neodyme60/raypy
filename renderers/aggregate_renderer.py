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
        Renderer.__init__(self, scene)

    def render_task(self, task_index: int, bucket_index: int, bucket_order_info: BucketOrderInfo, sample: Sample, color: int):
        pass

    def render(self, scene: Scene, bucket_order_info: BucketOrderInfo):
        pass

    def get_li(self, scene: Scene, sample: Sample, intersection: Intersection):
        pass