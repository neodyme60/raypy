import math


class Matrix44:
    __slots__ = ['data']

    def __init__(self):
        from maths.vector4d import Vector4d

        self.data = [Vector4d() for _ in range(4)]

    @staticmethod
    def create_from_vector4d(u, v, n, t):
        m = Matrix44()
        m.data[0].set_from_vector4d(u)
        m.data[1].set_from_vector4d(v)
        m.data[2].set_from_vector4d(n)
        m.data[3].set_from_vector4d(t)
        return m

    def __str__(self):
        s = ""
        for col in range(4):
            s += ("col(" + str(col) + ") " + str(self.data[col]) + '\n')
        return s

    def __len__(self):
        return 16

    def __getitem__(self, key):
        if 3 >= key >= 0:
            return self.data[key]
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Matrix44")

    def __setitem__(self, key: int, value: float):
        from maths.vector4d import Vector4d

        if type(value) is not Vector4d:
            raise IndexError("Invalid type " + str(key) + " to Vector4d")

        if 3 >= key >= 0:
            self.data[key] = value
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Matrix44")

    def set_to_zero(self):
        for i in range(4):
            self.data[i].set_to_zero()

    def get_transpose(self):
        obj = Matrix44()
        for i in range(4):
            for j in range(4):
                obj.data[j][i] = self.data[i][j]
        return obj

    def get_get(self, x, y):
        return self.data[y][x]

    # http://www.nigels.com/glt/doc/matrix4_8cpp-source.html
    def get_invert(self):
        tmp = Matrix44()

        mat = self

        m11 = mat.get_get(0, 0)
        m12 = mat.get_get(0, 1)
        m13 = mat.get_get(0, 2)
        m14 = mat.get_get(0, 3)
        m21 = mat.get_get(1, 0)
        m22 = mat.get_get(1, 1)
        m23 = mat.get_get(1, 2)
        m24 = mat.get_get(1, 3)
        m31 = mat.get_get(2, 0)
        m32 = mat.get_get(2, 1)
        m33 = mat.get_get(2, 2)
        m34 = mat.get_get(2, 3)
        m41 = mat.get_get(3, 0)
        m42 = mat.get_get(3, 1)
        m43 = mat.get_get(3, 2)
        m44 = mat.get_get(3, 3)

        d12 = (m31 * m42 - m41 * m32)
        d13 = (m31 * m43 - m41 * m33)
        d23 = (m32 * m43 - m42 * m33)
        d24 = (m32 * m44 - m42 * m34)
        d34 = (m33 * m44 - m43 * m34)
        d41 = (m34 * m41 - m44 * m31)

        tmp[0][0] = (m22 * d34 - m23 * d24 + m24 * d23)
        tmp[0][1] = -(m21 * d34 + m23 * d41 + m24 * d13)
        tmp[0][2] = (m21 * d24 + m22 * d41 + m24 * d12)
        tmp[0][3] = -(m21 * d23 - m22 * d13 + m23 * d12)

        # Compute determinant as early as possible using these cofactors.
        det = m11 * tmp[0][0] + m12 * tmp[0][1] + m13 * tmp[0][2] + m14 * tmp[0][3]

        # Run singularity test.
        if det == 0.0:
            # invert_matrix: Warning: Singular matrix.
            raise Exception("singular matrix !!, can not invert it")
        else:
            inv_det = 1.0 / det

            # Compute rest of inverse.
            tmp[0][0] *= inv_det
            tmp[0][1] *= inv_det
            tmp[0][2] *= inv_det
            tmp[0][3] *= inv_det

            tmp[1][0] = -(m12 * d34 - m13 * d24 + m14 * d23) * inv_det
            tmp[1][1] = (m11 * d34 + m13 * d41 + m14 * d13) * inv_det
            tmp[1][2] = -(m11 * d24 + m12 * d41 + m14 * d12) * inv_det
            tmp[1][3] = (m11 * d23 - m12 * d13 + m13 * d12) * inv_det

            # Pre-compute 2x2 dets for first two rows when computing
            # cofactors of last two rows.
            d12 = m11 * m22 - m21 * m12
            d13 = m11 * m23 - m21 * m13
            d23 = m12 * m23 - m22 * m13
            d24 = m12 * m24 - m22 * m14
            d34 = m13 * m24 - m23 * m14
            d41 = m14 * m21 - m24 * m11

            tmp[2][0] = (m42 * d34 - m43 * d24 + m44 * d23) * inv_det
            tmp[2][1] = -(m41 * d34 + m43 * d41 + m44 * d13) * inv_det
            tmp[2][2] = (m41 * d24 + m42 * d41 + m44 * d12) * inv_det
            tmp[2][3] = -(m41 * d23 - m42 * d13 + m43 * d12) * inv_det

            tmp[3][0] = -(m32 * d34 - m33 * d24 + m34 * d23) * inv_det
            tmp[3][1] = (m31 * d34 + m33 * d41 + m34 * d13) * inv_det
            tmp[3][2] = -(m31 * d24 + m32 * d41 + m34 * d12) * inv_det
            tmp[3][3] = (m31 * d23 - m32 * d13 + m33 * d12) * inv_det

            return tmp

    def __eq__(self, other):
        from maths.config import CONST_EPSILON

        if type(other) is not Matrix44:
            return NotImplemented

        for i in range(4):
            for j in range(4):
                if CONST_EPSILON < math.fabs(self.data[j][i] - other.data[j][i]):
                    return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        raise NotImplemented

    def __gt__(self, other):
        raise NotImplemented

    def __ge__(self, other):
        raise NotImplemented

    def __add__(self, other):
        obj = Matrix44()
        if type(other) == int or type(other) == float:
            for col in range(4):
                obj[col] = self[col] + other
        elif type(other) == Matrix44:
            for col in range(4):
                obj[col] = self[col] + other[col]
        else:
            raise NotImplemented
        return obj

    def __sub__(self, other):
        obj = Matrix44()
        if type(other) == int or type(other) == float:
            for col in range(4):
                obj[col] = self[col] - other
        elif type(other) == Matrix44:
            for col in range(4):
                obj[col] = self[col] - other[col]
        else:
            raise NotImplemented
        return obj

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            obj = Matrix44()
            for col in range(4):
                self[col] -= other
            return obj
        elif type(other) == Matrix44:
            obj = Matrix44()

            for j in range(4):
                for i in range(4):
                    for k in range(4):
                        obj[j][i] += self[j][k] * other[k][i]
            return obj
        raise NotImplemented
