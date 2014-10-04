from PIL import Image
from aggregates.simple import Simple
from core.intersection import Intersection
from core.ray import Ray


class Scene():

    def __init__(self, ):
        self.aggregate = Simple()

    def add_geometry(self, other):
        self.aggregate.add(other)

    def intersect(self, ray: Ray, intersection: Intersection):
        if self.aggregate.get_is_intersected(ray):
            return self.aggregate.get_intersection(ray, intersection)
        return False
