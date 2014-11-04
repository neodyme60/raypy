import math

from maths.point3d import Point3d
from maths.vector2d import Vector2d
from maths.vector3d import Vector3d


class Vector4d:
    __slots__ = ['x', 'y', 'z', 'w']

    def __init__(self, x: float=0.0, y: float=0.0, z: float=0.0, w: float=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def set_from_vector4d(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z
        self.w = other.w
        return self

    @staticmethod
    def create_from_vector2d(other: Vector2d, z: float=0.0, w: float=0.0):
        return Vector4d(other.x, other.y, z, w)

    @staticmethod
    def create_from_vector3d(other: Vector3d, w: float=0.0):
        return Vector4d(other.x, other.y, other.z, w)

    @staticmethod
    def create_from_point3d(other: Point3d, w: float=0.0):
        return Vector4d(other.x, other.y, other.z, w)

    @staticmethod
    def create_from_vector4d(other):
        return Vector4d(other.x, other.y, other.z, other.w)

    @staticmethod
    def dot(a, b) -> float:
        assert type(a) == Vector4d
        assert type(b) == Vector4d
        return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

    def get_length(self) -> float:
        return math.sqrt(self.get_length_squared())

    def get_length_squared(self) -> float:
        return Vector4d.dot(self, self)

    def set_to_zero(self):
        self.x = self.y = self.z = self.w = 0.0

    # Unary operator
    def __neg__(self):
        return Vector4d(-self.x, -self.y, -self.z, -self.w)

    def __len__(self):
        return 4

    def __eq__(self, other):
        from maths.config import CONST_EPSILON

        if type(other) is not Vector4d:
            return NotImplemented

        if (self - other).get_length_squared() <= CONST_EPSILON:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        raise NotImplemented

    def __gt__(self, other):
        raise NotImplemented

    def __ge__(self, other):
        raise NotImplemented

    def __getitem__(self, key) -> float:
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        elif key == 3:
            return self.w
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Vec3d")

    def __setitem__(self, key: int, value: float):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        elif key == 3:
            self.w = value
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Vec3d")

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(self.w)

    def __mul__(self, other):
        from maths.matrix44 import Matrix44
        from core.transform import Transform

        if type(other) == int or type(other) == float:
            return Vector4d(self.x * other, self.y * other, self.z * other, self.w * other)
        elif type(other) == Vector4d:
            return Vector4d(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
        elif type(other) == Matrix44:
            return Vector4d(
                self.x * other[0][0] + self.y * other[1][0] + self.z * other[2][0] + self.w * other[3][0],
                self.x * other[0][1] + self.y * other[1][1] + self.z * other[2][1] + self.w * other[3][1],
                self.x * other[0][2] + self.y * other[1][2] + self.z * other[2][2] + self.w * other[3][2],
                self.x * other[0][3] + self.y * other[1][3] + self.z * other[2][3] + self.w * other[3][3]
            )
        elif type(other) == Transform:
            return self * other.mat
        else:
            raise NotImplemented

    def __imul__(self, other):
        if type(other) == int or type(other) == float:
            self.x *= other
            self.y *= other
            self.z *= other
            self.w *= other
            return self
        elif type(other) == Vector4d:
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
            self.w *= other.w
            return self
        else:
            raise NotImplemented

    def __add__(self, other):
        from maths.vector3d import Vector3d
        from maths.vector2d import Vector2d

        if type(other) == int or type(other) == float:
            return Vector4d(self.x + other, self.y + other, self.z + other, self.w + other)
        elif type(other) == Vector4d:
            return Vector4d(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
        elif type(other) == Vector3d:
            return Vector4d(self.x + other.x, self.y + other.y, self.z + other.z, self.w)
        elif type(other) == Vector2d:
            return Vector4d(self.x + other.x, self.y + other.y, self.z, self.w)
        else:
            raise NotImplemented

    def __iadd__(self, other):
        from maths.vector3d import Vector3d
        from maths.vector2d import Vector2d

        if type(other) == int or type(other) == float:
            self.x += other
            self.y += other
            self.z += other
            self.w += other
            return self
        elif type(other) == Vector4d:
            self.x += other.x
            self.y += other.y
            self.z += other.z
            self.w += other.w
            return self
        elif type(other) == Vector3d:
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        elif type(other) == Vector2d:
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise NotImplemented

    def __sub__(self, other):
        from maths.vector3d import Vector3d
        from maths.vector2d import Vector2d

        if type(other) == int or type(other) == float:
            return Vector4d(self.x - other, self.y - other, self.z - other, self.w - other)
        elif type(other) == Vector4d:
            return Vector4d(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
        elif type(other) == Vector3d:
            return Vector4d(self.x - other.x, self.y - other.y, self.z - other.z, self.w)
        elif type(other) == Vector2d:
            return Vector4d(self.x - other.x, self.y - other.y, self.z, self.w)
        else:
            raise NotImplemented

    def __isub__(self, other):
        from maths.vector3d import Vector3d
        from maths.vector2d import Vector2d

        if type(other) == int or type(other) == float:
            self.x -= other
            self.y -= other
            self.z -= other
            self.w -= other
            return self
        elif type(other) == Vector4d:
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            self.w -= other.w
            return self
        elif type(other) == Vector3d:
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        elif type(other) == Vector2d:
            self.x -= other.x
            self.y -= other.y
            return self
        else:
            raise NotImplemented