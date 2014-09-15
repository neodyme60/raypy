import sys

from intersection import Intersection
from core.shape import Shape
from maths.vector3d import Vector3d


__author__ = 'nicolas'

class Plane(Shape):

    #plan in form ax+by+cz+d=0

    def __init__(self):
        self.normal=Vector3d.get_up()
        self.distance=0.0

    def get_intersection(self, ray):
        denom = self.normal.dot(ray.direction)
        if denom > 1e-6:
            t = -(self.normal.dot(ray.origin)+self.distance) / denom
            if t >= 0.0 and t<sys.float_info.max:
                i = Intersection()
                i.distance = t
                i.intersection = ray.origin + ray.direction * t
                i.normal = self.normal
                return i
        return None
