import math

class Vector4d:

    __slots__ = ['x', 'y', 'z', 'w']

    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0, w:float=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @staticmethod
    def createFromVector2d(other, z:float=0.0, w:float=0.0):
        return Vector4d(other.x, other.y, z, w)

    @staticmethod
    def createFromVector3d(other, w:float=0.0):
        return Vector4d(other.x, other.y, other.z, w)

    @staticmethod
    def createFromPoint3d(other):
        return Vector4d(other.x, other.y, other.z, 1.0)

    @staticmethod
    def createFromVector4d(other):
        return Vector4d(other.x, other.y, other.z, other.w)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def get_length(self)->float:
        return math.sqrt(self.get_length_squared())

    def get_length_squared(self)->float:
        return self.dot(self)

    def set_to_zero(self):
        self.x = self.y = self.z = self.w = 0.0

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

    def __getitem__(self, key)->float:
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
            obj = Vector4d()
            mat_transpose = other.get_transpose()
            for col in range(0, 4):
                obj[col] = mat_transpose[col].dot(self)
            return obj
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