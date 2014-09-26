__author__ = 'nicolas'


class Normal:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x: float=0.0, y: float=0.0, z: float=0.0):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def create_from_vector3d(other):
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
