from maths.config import infinity_max_f
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.transform import Transform


class Ray:

    __slots__ = ['origin', 'direction', 'depth', 'max_t', 'min_t', 'time']

    def __init__(self, origin: Point3d=Point3d(0.0, 0.0, 0.0), direction:Vector3d=Vector3d.get_forward(), min_t: float=0.0, max_t: float=infinity_max_f, time: float=0.0, depth: int=0):

        self.origin = origin
        self.direction = direction
        self.depth = depth
        self.max_t = max_t
        self.min_t = min_t
        self.time = time

    def get_at(self, other: float):
        return self.origin + (self.direction * other)

    def __mul__(self, other: Transform):
        return Ray(self.origin * other, self.direction * other, self.min_t, self.max_t, self.time, self.depth)