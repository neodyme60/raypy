import math
from core.transform import Transform
from maths.matrix44 import Matrix44

__author__ = 'nicolas'


class Normal:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x: float=0.0, y: float=0.0, z: float=0.0):
        self.x = x
        self.y = y
        self.z = z

    def Set(self, n):
        self.x = n.x
        self.y = n.y
        self.z = n.z
        return self

    @staticmethod
    def create_from_vector3d(other):
        return Normal(other.x, other.y, other.z)

    @staticmethod
    def create_from_point3d(other):
        return Normal(other.x, other.y, other.z)

    def __add__(self, other):
        from maths.vector3d import Vector3d

        if type(other) is Vector3d:
            return Normal(self.x + other.x, self.y + other.y, self.z + other.z)
        raise NotImplemented

    def __sub__(self, other):
        from maths.vector3d import Vector3d

        if type(other) is Vector3d:
            return Normal(self.x - other.x, self.y - other.y, self.z - other.z)
        raise NotImplemented

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Normal(self.x * other, self.y * other, self.z * other)
        elif type(other) == Normal:
            return Normal(self.x * other.x, self.y * other.y, self.z * other.z)
        elif type(other) == Matrix44:
            return Normal(
                self.x * other[0][0] + self.y * other[1][0] + self.z * other[2][0],
                self.x * other[0][1] + self.y * other[1][1] + self.z * other[2][1],
                self.x * other[0][2] + self.y * other[1][2] + self.z * other[2][2]
            )
        elif type(other) == Transform:
            return self * other.mat
        else:
            raise NotImplemented

    @staticmethod
    def dot(a, b) -> float:
        return a.x * b.x + a.y * b.y + a.z * b.z

    def get_length(self) -> float:
        return math.sqrt(self.get_length_squared())

    def get_length_squared(self) -> float:
        return Normal.dot(self, self)

    def get_normalized(self):
        t = self.get_length()
        if t == 0:
            raise ZeroDivisionError
        d = 1.0 / t
        return Normal(self.x * d, self.y * d, self.z * d)
