from maths.matrix44 import Matrix44
from core.transform import Transform


class Point3d:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x: float=0.0, y: float=0.0, z: float=0.0):
        self.x = x
        self.y = y
        self.z = z

    def Set(self, p):
        self.x = p.x
        self.y = p.y
        self.z = p.z
        return self

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

    def __eq__(self, other):
        from maths.config import CONST_EPSILON

        if type(other) is not Point3d:
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
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Vec3d")

    @staticmethod
    def create_from_vector3d(other):
        return Point3d(other.x, other.y, other.z)

    @staticmethod
    def create_from_vector4d(other):
        if other.w == 0.0:
            raise ZeroDivisionError
        w_inv = 1.0 / other.w
        return Point3d(other.x * w_inv, other.y * w_inv, other.z * w_inv)

    def __add__(self, other):
        from maths.vector3d import Vector3d

        if type(other) == Vector3d:
            return Point3d(self.x + other.x, self.y + other.y, self.z + other.z)
        if type(other) == Point3d:
            return Point3d(self.x + other.x, self.y + other.y, self.z + other.z)
        raise NotImplemented

    def __iadd__(self, other):
        from maths.vector3d import Vector3d

        if type(other) == Vector3d:
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            raise NotImplemented

    def __sub__(self, other):
        from maths.vector3d import Vector3d

        if type(other) == Vector3d:
            return Point3d(self.x - other.x, self.y - other.y, self.z - other.z)
        elif type(other) == Point3d:
            return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)
        raise NotImplemented

    def __isub__(self, other):
        from maths.vector3d import Vector3d

        if type(other) == Vector3d:
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            raise NotImplemented

    def __div__(self, other):
        from maths.vector3d import Vector3d

        if type(other) == Vector3d or type(other) == Point3d:
            return Point3d(self.x / other.x, self.y / other.y, self.z / other.z)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Point3d(self.x * other, self.y * other, self.z * other)
        elif type(other) == Matrix44:
            return Point3d(
                self.x * other[0][0] + self.y * other[1][0] + self.z * other[2][0] + other[3][0],
                self.x * other[0][1] + self.y * other[1][1] + self.z * other[2][1] + other[3][1],
                self.x * other[0][2] + self.y * other[1][2] + self.z * other[2][2] + other[3][2],
            )
        elif type(other) == Transform:
            return self * other.mat
        raise NotImplemented