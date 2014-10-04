import math
from maths.matrix44 import Matrix44
from maths.vector3d import Vector3d


class Transform:
    def __init__(self, mat: Matrix44, mat_inv: Matrix44=None):
        self.mat = mat
        if mat_inv is None:
            self.mat_inv = mat.get_invert()
        else:
            self.mat_inv = mat_inv

    def __str__(self):
        return "====>mat:\n" + str(self.mat) + "\nmat inv:\n" + str(self.mat_inv) + "<======"

    def get_invert(self):
        t = Transform(self.mat_inv, self.mat)
        return t

    def __eq__(self, other):
        assert type(other) == Transform
        return self.mat == other.mat and self.mat_inv == other.mat_inv

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        raise NotImplemented

    def __gt__(self, other):
        raise NotImplemented

    def __ge__(self, other):
        raise NotImplemented

    def __mul__(self, other):
        assert type(other) == Transform
        # invert of matrix product is :  (AxB)-1 = B-1 x A-1
        # see: https://proofwiki.org/wiki/Inverse_of_Matrix_Product
        return Transform(self.mat * other.mat, other.mat_inv * self.mat_inv)

    @staticmethod
    def create_identity():
        from maths.matrix44 import Matrix44
        from maths.vector4d import Vector4d

        m = Matrix44.create_from_vector4d(Vector4d(1.0, 0.0, 0.0, 0.0), Vector4d(0.0, 1.0, 0.0, 0.0),
                                          Vector4d(0.0, 0.0, 1.0, 0.0), Vector4d(0.0, 0.0, 0.0, 1.0))
        return Transform(m, m)

    @staticmethod
    def create_scale(x=None, y=None, z=None):
        from maths.matrix44 import Matrix44
        from maths.vector3d import Vector3d
        from maths.vector4d import Vector4d

        if type(x) == Vector3d:
            m = Matrix44.create_from_vector4d(Vector4d(x.x, 0.0, 0.0, 0.0),
                                              Vector4d(0.0, x.y, 0.0, 0.0),
                                              Vector4d(0.0, 0.0, x.z, 0.0),
                                              Vector4d(0.0, 0.0, 0.0, 1.0))
            m_inv = Matrix44.create_from_vector4d(Vector4d(1.0 / x.x, 0.0, 0.0, 0.0),
                                                  Vector4d(0.0, 1.0 / x.y, 0.0, 0.0),
                                                  Vector4d(0.0, 0.0, 1.0 / x.z, 0.0),
                                                  Vector4d(0.0, 0.0, 0.0, 1.0))
        else:
            m = Matrix44.create_from_vector4d(Vector4d(x, 0.0, 0.0, 0.0),
                                              Vector4d(0.0, y, 0.0, 0.0),
                                              Vector4d(0.0, 0.0, z, 0.0),
                                              Vector4d(0.0, 0.0, 0.0, 1.0))
            m_inv = Matrix44.create_from_vector4d(Vector4d(1.0 / x, 0.0, 0.0, 0.0),
                                                  Vector4d(0.0, 1.0 / y, 0.0, 0.0),
                                                  Vector4d(0.0, 0.0, 1.0 / z, 0.0),
                                                  Vector4d(0.0, 0.0, 0.0, 1.0))
        return Transform(m, m_inv)

    @staticmethod
    def create_translate(x=None, y=None, z=None):
        from maths.matrix44 import Matrix44
        from maths.vector3d import Vector3d
        from maths.vector4d import Vector4d

        if type(x) == Vector3d:
            m = Matrix44.create_from_vector4d(Vector4d(1.0, 0.0, 0.0, 0.0),
                                              Vector4d(0.0, 1.0, 0.0, 0.0),
                                              Vector4d(0.0, 0.0, 1.0, 0.0),
                                              Vector4d(x.x, x.y, x.z, 1.0))

            m_inv = Matrix44.create_from_vector4d(Vector4d(1.0, 0.0, 0.0, 0.0),
                                                  Vector4d(0.0, 1.0, 0.0, 0.0),
                                                  Vector4d(0.0, 0.0, 1.0, 0.0),
                                                  Vector4d(-x.x, -x.y, -x.z, 1.0))
        else:
            m = Matrix44.create_from_vector4d(Vector4d(1.0, 0.0, 0.0, 0.0),
                                              Vector4d(0.0, 1.0, 0.0, 0.0),
                                              Vector4d(0.0, 0.0, 1.0, 0.0),
                                              Vector4d(x, y, z, 1.0))
            m_inv = Matrix44.create_from_vector4d(Vector4d(1.0, 0.0, 0.0, 0.0),
                                                  Vector4d(0.0, 1.0, 0.0, 0.0),
                                                  Vector4d(0.0, 0.0, 1.0, 0.0),
                                                  Vector4d(-x, -y, -z, 1.0))
        return Transform(m, m_inv)

    @staticmethod
    def create_rot_x(angle: float):
        from maths.matrix44 import Matrix44
        from maths.vector4d import Vector4d

        c = math.cos(angle)
        s = math.sin(angle)
        m = Matrix44.create_from_vector4d(Vector4d(1.0, 0.0, 0.0, 0.0),
                                          Vector4d(0.0, c, s, 0.0),
                                          Vector4d(0.0, -s, c, 0.0),
                                          Vector4d(0.0, 0.0, 0.0, 1.0))
        return Transform(m, m.get_transpose())

    @staticmethod
    def create_rot_y(angle):
        from maths.matrix44 import Matrix44
        from maths.vector4d import Vector4d

        c = math.cos(angle)
        s = math.sin(angle)
        m = Matrix44.create_from_vector4d(Vector4d(c, 0.0, -s, 0.0),
                                          Vector4d(0.0, 1.0, 0.0, 0.0),
                                          Vector4d(s, 0.0, c, 0.0),
                                          Vector4d(0.0, 0.0, 0.0, 1.0))
        return Transform(m, m.get_transpose())

    @staticmethod
    def create_rot_z(angle):
        from maths.matrix44 import Matrix44
        from maths.vector4d import Vector4d

        c = math.cos(angle)
        s = math.sin(angle)
        m = Matrix44.create_from_vector4d(Vector4d(c, s, 0.0, 0.0),
                                          Vector4d(-s, c, 0.0, 0.0),
                                          Vector4d(0.0, 0.0, 1.0, 0.0),
                                          Vector4d(0.0, 0.0, 0.0, 1.0))
        return Transform(m, m.get_transpose())

    @staticmethod
    def create_look_at(eye, at, up):
        from maths.matrix44 import Matrix44
        from maths.vector4d import Vector4d

        # Initialize first three columns of viewing matrix
        z_axis = (at - eye).get_normalized()
        x_axis = Vector3d.cross(up, z_axis).get_normalized()
        y_axis = Vector3d.cross(z_axis, x_axis)

        m = Matrix44.create_from_vector4d(
            Vector4d.create_from_vector3d(x_axis, -Vector3d.dot(x_axis, eye)),
            Vector4d.create_from_vector3d(y_axis, -Vector3d.dot(y_axis, eye)),
            Vector4d.create_from_vector3d(z_axis, -Vector3d.dot(z_axis, eye)),
            Vector4d.create_from_vector3d(eye, 1.0)
        )
        return Transform(m)

    @staticmethod
    def create_orthographic(z_near: float, z_far: float):
        return Transform.create_translate(0.0, 0.0, -z_near) * Transform.create_scale(1.0, 1.0, 1.0 / (z_far - z_near))

    @staticmethod
    def create_perspective(fov: float=90, z_near: float=0.0, z_far: float=1.0):
        from maths.matrix44 import Matrix44
        from maths.vector4d import Vector4d

        inv = 1.0 / (z_far - z_near)

        # Perform projective divide
        perspective_matrix = Matrix44.create_from_vector4d(
            Vector4d(1.0, 0.0, 0.0, 0.0),
            Vector4d(0.0, 1.0, 0.0, 0.0),
            Vector4d(0.0, 0.0, z_far * inv, 1.0),
            Vector4d(0.0, 0.0, -z_far * z_near * inv, 0.0)
        )

        # Scale to canonical viewing volume
        inv_tan = 1.0 / math.tan(math.radians(fov) * 0.5)

        return Transform(perspective_matrix) * Transform.create_scale(inv_tan, inv_tan, 1.0)
