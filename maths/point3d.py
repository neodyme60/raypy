class Point3d:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

    def __eq__(self, other):
        from maths.config import CONST_EPSILON
        if type(other) is not Point3d:
            return NotImplemented

        if (self-other).get_length_squared() <= CONST_EPSILON:
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

    @staticmethod
    def createFromVector3d(other):
        return Point3d(other.x, other.y, other.z)

    @staticmethod
    def createFromVector4d(other):
        if other.w == 0.0:
            raise ZeroDivisionError
        w_inv = 1.0 / other.w
        return Point3d(other.x * w_inv, other.y * w_inv, other.z * w_inv)

    def __add__(self, other):
        from maths.vector3d import Vector3d

        if type(other) == Vector3d:
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

    def __mul__(self, other):
        from maths.vector4d import Vector4d
        a = Vector4d.createFromPoint3d(self)
        v = a * other.mat
        w_inv = 1.0 / v.w
        return Point3d(v.x * w_inv, v.y * w_inv, v.z * w_inv)