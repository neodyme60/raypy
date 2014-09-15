import sys

from maths.vector3d import Vector3d
from point3d import Point3d
from core.transform import Transform


class Ray:
    def __init__(self, origin=None, direction=None, min_t=0.0, max_t=sys.float_info.max, time=0.0, depth=0):
        if type(origin) is None:
            self.origin = Point3d(0.0, 0.0, 0.0)
        else:
            self.origin = Point3d(origin.x, origin.y, origin.z)

        if type(direction) is None:
            self.direction = Vector3d.get_forward()
        else:
            self.origin = Vector3d(direction.x, direction.y, direction.z)
        self.depth = depth
        self.max_t = min_t
        self.min_t = max_t
        self.time = time

    def get_at(self, other):
        if type(other) == float:
            return self.origin + (self.direction*other)
        raise NotImplemented

    def __mul__(self, other):
        if type(other)==Transform:
            return  Ray(self.origin * other, self.direction * other, self.min_t, self.max_t, self.time, self.depth)
        else:
            raise NotImplemented

