import math
from maths.matrix44 import Matrix44
from core.transform import Transform

class Vector3d:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x: float=0.0, y: float=0.0, z: float=0.0):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def create_from_vector2d(other, z: float=0.0):
        return Vector3d(other.x, other.y, z)

    @staticmethod
    def create_from_vector3d(other):
        return Vector3d(other.x, other.y, other.z)

    @staticmethod
    def create_from_point3d(other):
        return Vector3d(other.x, other.y, other.z)

    @staticmethod
    def create_from_vector4d(other):
        return Vector3d(other.x, other.y, other.z)

    def dot(self, other) -> float:
        assert type(other) == Vector3d
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3d((self.y * other.z) - (self.z * other.y),
                        (self.z * other.x) - (self.x * other.z),
                        (self.x * other.y) - (self.y * other.x))

    @staticmethod
    def get_up():
        return Vector3d(0.0, 1.0, 0.0)

    @staticmethod
    def get_down():
        return Vector3d(0.0, -1.0, 0.0)

    @staticmethod
    def get_left():
        return Vector3d(-1.0, 0.0, 0.0)

    @staticmethod
    def get_right():
        return Vector3d(1.0, 0.0, 0.0)

    @staticmethod
    def get_forward():
        return Vector3d(0.0, 0.0, 1.0)

    @staticmethod
    def get_backward():
        return Vector3d(0.0, 0.0, -1.0)

    def get_length(self) -> float:
        return math.sqrt(self.get_length_squared())

    def get_length_squared(self) -> float:
        return self.dot(self)

    def set_to_zero(self):
        self.x = self.y = self.z = 0.0

    # Unary operator
    def __neg__(self):
        return Vector3d(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        from maths.config import CONST_EPSILON

        if type(other) is not Vector3d:
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

    def __setitem__(self, key: int, value: float):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Vec3d")

    def __len__(self):
        return 3

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3d(self.x * other, self.y * other, self.z * other)
        elif type(other) == Vector3d:
            return Vector3d(self.x * other.x, self.y * other.y, self.z * other.z)
        elif type(other) == Matrix44:
            return Vector3d(
                self.x * other[0][0] + self.y * other[1][0] + self.z * other[2][0],
                self.x * other[0][1] + self.y * other[1][1] + self.z * other[2][1],
                self.x * other[0][2] + self.y * other[1][2] + self.z * other[2][2]
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
            return self
        elif type(other) == Vector3d:
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
            return self
        else:
            raise NotImplemented

    def __add__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector2d import Vector2d

        if type(other) == int or type(other) == float:
            return Vector3d(self.x + other, self.y + other, self.z + other)
        elif type(other) == Vector4d or type(other) == Vector3d:
            return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)
        elif type(other) == Vector2d:
            return Vector3d(self.x + other.x, self.y + other.y, self.z)
        else:
            raise NotImplemented

    def __iadd__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector2d import Vector2d

        if type(other) == int or type(other) == float:
            self.x += other
            self.y += other
            self.z += other
            return self
        elif type(other) == Vector4d or type(other) == Vector3d:
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
        from maths.vector4d import Vector4d
        from maths.vector2d import Vector2d

        if type(other) == int or type(other) == float:
            return Vector3d(self.x - other, self.y - other, self.z - other)
        elif type(other) == Vector4d or type(other) == Vector3d:
            return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)
        elif type(other) == Vector2d:
            return Vector3d(self.x - other.x, self.y - other.y, self.z)
        else:
            raise NotImplemented

    def __isub__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector2d import Vector2d

        if type(other) == int or type(other) == float:
            self.x -= other
            self.y -= other
            self.z -= other
            return self
        elif type(other) == Vector4d or type(other) == Vector3d:
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

    def get_normalized(self):
        t = self.get_length()
        if t == 0:
            raise ZeroDivisionError
        d = 1.0 / math.sqrt(t)
        return Vector3d(self.x * d, self.y * d, self.z * d)
