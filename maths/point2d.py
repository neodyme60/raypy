class Point2d:
    __slots__ = ['x', 'y']

    def __init__(self, x:float=0.0, y:float=0.0):
        from maths.vector4d import Vector4d
        from maths.vector3d import Vector3d
        from maths.vector2d import Vector2d
        from maths.point3d import Point3d
        if type(x) is Point2d or type(x) is Vector2d:
            self.x = x.x
            self.y = x.y
        elif type(x) is Point3d or type(x) is Vector3d or type(x) is Vector4d:
            self.x = x.x
            self.y = x.y
        else:
            if x is None:
                self.x = 0.0
            else:
                self.x = x
            if y is None:
                self.y = 0.0
            else:
                self.y = y

    def __add__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector3d import Vector3d
        from maths.vector2d import Vector2d

        obj = Point2d()
        if type(other) == Vector4d or type(other) == Vector3d or type(other) == Vector2d:
            obj.x = other.x + self.x
            obj.y = other.y + self.y
            return obj
        else:
            raise NotImplemented

    def __iadd__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector3d import Vector3d
        from maths.vector2d import Vector2d

        if type(other) == Vector4d or type(other) == Vector3d or type(other) == Vector2d:
            self.x += other.x
            self.y += other.y
        else:
            raise NotImplemented

    def __sub__(self, other):
        from maths.vector4d import Vector4d
        from maths.vector3d import Vector3d
        from maths.vector2d import Vector2d

        obj = Point2d()
        if type(other) == Vector4d or type(other) == Vector3d or type(other) == Vector2d:
            obj.x = self.x - other.x
            obj.y = self.y - other.y
            return obj
        else:
            raise NotImplemented

    def __isub_(self, other):
        from maths.vector4d import Vector4d
        from maths.vector3d import Vector3d
        from maths.vector2d import Vector2d

        if type(other) == Vector4d or type(other) == Vector3d or type(other) == Vector2d:
            self.x -= other.x
            self.y -= other.y
        else:
            raise NotImplemented