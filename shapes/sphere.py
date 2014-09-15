import sys
import maths
from core.shape import Shape
from maths.vector3d import Vector3d
from core.intersection import Intersection

class Sphere(Shape):

    def __init__(self):
        self.center = Vector3d(0.0, 0.0, 0.0)
        self.radius = 1.0
        self.radius_squared = 1.0

    def get_intersection(self, ray):
        e = self.center - ray.origin
        a = ray.direction.dot(e)

        f = self.radius_squared - e.dot(e) + (a * a)
        if f<0.0:
            i = None
        else:
            t = a - maths.sqrt(f)
            if t > 0.1 and t < sys.float_info.max:
                i=Intersection()
                i.distance = t
                i.intersection = ray.origin + ray.direction * t
                i.normal = (i.intersection-self.center).get_normalized()
        return i


