import math


class Vector2d:
    __slots__ = ['x', 'y']

    def __init__(self, x: float=0.0, y: float=0.0):
        self.x = x
        self.y = y

    @staticmethod
    def create_from_vector2d(other):
        return Vector2d(other.x, other.y)

    @staticmethod
    def create_from_vector3d(other):
        return Vector2d(other.x, other.y)

    @staticmethod
    def create_from_vector4d(other):
        return Vector2d(other.x, other.y)

    def get_length(self) -> float:
        return math.sqrt(self.get_length_squared())

    def get_length_squared(self) -> float:
        return Vector2d.dot(self, self)

    @staticmethod
    def dot(a, b) -> float:
        assert type(a) == Vector2d
        assert type(b) == Vector2d
        return a.x * b.x + a.y * b.y

    def set_to_zero(self):
        self.x = self.y = 0.0

    def __len__(self):
        return 2

    # Unary operator
    def __neg__(self):
        return Vector2d(-self.x, -self.y)

    def __getitem__(self, key) -> float:
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Vec3d")

    def __eq__(self, other):
        from maths.config import CONST_EPSILON

        if type(other) is not Vector2d:
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

    def __setitem__(self, key: int, value: float):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Vec3d")

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2d(self.x * other, self.y * other)
        elif type(other) == Vector2d:
            return Vector2d(self.x * other.x, self.y * other.y)
        else:
            raise NotImplemented

    def __imul__(self, other):
        if type(other) == int or type(other) == float:
            self.x *= other
            self.y *= other
            return self
        elif type(other) == Vector2d:
            self.x *= other.x
            self.y *= other.y
            return self
        else:
            raise NotImplemented

    def __add__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector3d import Vector3d

        if type(other) == int or type(other) == float:
            return Vector2d(self.x + other, self.y + other)
        elif type(other) == Vector4d or type(other) == Vector3d or type(other) == Vector2d:
            return Vector2d(self.x + other.x, self.y + other.y)
        else:
            raise NotImplemented

    def __iadd__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector3d import Vector3d

        if type(other) == int or type(other) == float:
            self.x += other
            self.y += other
            return self
        elif type(other) == Vector4d or type(other) == Vector3d or type(other) == Vector2d:
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise NotImplemented

    def __sub__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector3d import Vector3d

        if type(other) == int or type(other) == float:
            return Vector2d(self.x - other, self.y - other)
        elif type(other) == Vector4d or type(other) == Vector3d or type(other) == Vector2d:
            return Vector2d(self.x - other.x, self.y - other.y)
        else:
            raise NotImplemented

    def __isub__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector3d import Vector3d

        if type(other) == int or type(other) == float:
            self.x -= other
            self.y -= other
            return self
        elif type(other) == Vector4d or type(other) == Vector3d or type(other) == Vector2d:
            self.x -= other.x
            self.y -= other.y
            return self
        else:
            raise NotImplemented