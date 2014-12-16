from core.intersection import Intersection
from core.ray import Ray
from core.volume_region import VolumeRegion


class Scene():

    def __init__(self, accelerator, lights, volume_region: VolumeRegion):
        self.volume_region = volume_region
        self.aggregate = accelerator
        self.lights = lights

    def get_intersection(self, ray: Ray, intersection: Intersection)->bool:
        if self.aggregate.get_is_intersected(ray):
            return self.aggregate.get_intersection(ray, intersection)
        return False

    def get_is_intersected(self, ray: Ray)->bool:
        return self.aggregate.get_is_intersected(ray)
