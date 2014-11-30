from core.buckets import BucketOrderInfo
from core.intersection import Intersection
from core.ray import Ray
from core.sample import Sample
from core.scene import Scene
from core.spectrum import Spectrum


class Renderer:
    def __init__(self):
        pass

    def render(self, scene, bucket_order_info: BucketOrderInfo, multiThread: bool=True):
        raise NotImplementedError

    def render_task(self, task_index: int,
                    bucket_index: int,
                    bucket_order_info: BucketOrderInfo, sample, renderer):
        raise NotImplementedError

    def get_li(self, scene, ray: Ray, intersection: Intersection, sample: Sample)->Spectrum:
        pass

    def Transmittance(self, scene: Scene, ray: Ray, sample: Sample)->Spectrum:
        raise NotImplementedError
