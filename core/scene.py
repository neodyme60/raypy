from core.intersection import Intersection
from core.light import Light
from core.primitive import Primitive
from core.ray import Ray
from core.volume_region import VolumeRegion


class Scene():

    def __init__(self, accelerator: Primitive, lights: [Light], volume_region: VolumeRegion):
        self.volume_region = volume_region
        self.aggregate = accelerator
        self.lights = lights

    def get_intersection(self, ray: Ray, intersection: Intersection):
        if self.aggregate.get_is_intersected(ray):
            return self.aggregate.get_intersection(ray, intersection)
        return False

    def get_is_intersected(self, ray: Ray):
        return self.aggregate.get_is_intersected(ray)
