import sys
from core.intersection import Intersection
from core.shape import Shape
from maths.vector3d import Vector3d
from core.ray import Ray


class Plane(Shape):
    # plan in form ax+by+cz+d=0

    def __init__(self, o2w, w2o):
        Shape.__init__(self, o2w, w2o)
        self.normal = Vector3d.get_up()
        self.distance = 0.0

    def get_intersection(self, ray:Ray) -> Intersection:
        denom = self.normal.dot(ray.direction)
        if denom > 1e-6:
            t = -(self.normal.dot(ray.origin) + self.distance) / denom
            if 0.0 <= t < ray.max_t:
                i = Intersection()
                i.distance = t
                i.intersection = ray.origin + ray.direction * t
                i.normal = self.normal
                return i
        return None
