import math
import maths

inline_math_mult = False

class Matrix44:
    __slots__ = ['data']

    def __init__(self):
        from maths.vector4d import Vector4d
        self.data = [Vector4d() for i in range(4)]

    @staticmethod
    def create_from_vector4d(u, v, n, t):
        m = Matrix44()
        m.data[0] = u
        m.data[1] = v
        m.data[2] = n
        m.data[3] = t
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

    # http://www.nigels.com/glt/doc/matrix4_8cpp-source.html
    def get_invert(self):
        tmp = Matrix44()

        # we use row major, this code is for open GL column major, so we transpose...
        mat = self.get_transpose()

        d01 = mat[2][0] * mat[3][1] - mat[3][0] * mat[2][1]
        d02 = mat[2][0] * mat[3][2] - mat[3][0] * mat[2][2]
        d12 = mat[2][1] * mat[3][2] - mat[3][1] * mat[2][2]
        d13 = mat[2][1] * mat[3][3] - mat[3][1] * mat[2][3]
        d23 = mat[2][2] * mat[3][3] - mat[3][2] * mat[2][3]
        d30 = mat[2][3] * mat[3][0] - mat[3][3] * mat[2][0]

        tmp[0][0] = (mat[1][1] * d23 - mat[1][2] * d13 + mat[1][3] * d12)
        tmp[0][1] = -(mat[1][0] * d23 + mat[1][2] * d30 + mat[1][3] * d02)
        tmp[0][2] = (mat[1][0] * d13 + mat[1][1] * d30 + mat[1][3] * d01)
        tmp[0][3] = -(mat[1][0] * d12 - mat[1][1] * d02 + mat[1][2] * d01)

        # Compute determinant as early as possible using these cofactors.
        det = mat[0][0] * tmp[0][0] + mat[0][1] * tmp[0][1] + mat[0][2] * tmp[0][2] + mat[0][3] * tmp[0][3]

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

            tmp[1][0] = -(mat[0][1] * d23 - mat[0][2] * d13 + mat[0][3] * d12) * inv_det
            tmp[1][1] = (mat[0][0] * d23 + mat[0][2] * d30 + mat[0][3] * d02) * inv_det
            tmp[1][2] = -(mat[0][0] * d13 + mat[0][1] * d30 + mat[0][3] * d01) * inv_det
            tmp[1][3] = (mat[0][0] * d12 - mat[0][1] * d02 + mat[0][2] * d01) * inv_det

            # Pre-compute 2x2 dets for first two rows when computing
            # cofactors of last two rows.
            d01 = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
            d02 = mat[0][0] * mat[1][2] - mat[1][0] * mat[0][2]
            d12 = mat[0][1] * mat[1][2] - mat[1][1] * mat[0][2]
            d13 = mat[0][1] * mat[1][3] - mat[1][1] * mat[0][3]
            d23 = mat[0][3] * mat[1][3] - mat[1][2] * mat[0][3]
            d30 = mat[0][3] * mat[1][0] - mat[1][3] * mat[0][0]

            tmp[2][0] = (mat[3][1] * d23 - mat[3][2] * d13 + mat[3][3] * d12) * inv_det
            tmp[2][1] = -(mat[3][0] * d23 + mat[3][2] * d30 + mat[3][3] * d02) * inv_det
            tmp[2][2] = (mat[3][0] * d13 + mat[3][1] * d30 + mat[3][3] * d01) * inv_det
            tmp[2][3] = -(mat[3][0] * d12 - mat[3][1] * d02 + mat[3][2] * d01) * inv_det

            tmp[3][0] = -(mat[2][1] * d23 - mat[2][2] * d13 + mat[2][3] * d12) * inv_det
            tmp[3][1] = (mat[2][0] * d23 + mat[2][2] * d30 + mat[2][3] * d02) * inv_det
            tmp[3][2] = -(mat[2][0] * d13 + mat[2][1] * d30 + mat[2][3] * d01) * inv_det
            tmp[3][3] = (mat[2][0] * d12 - mat[2][1] * d02 + mat[2][2] * d01) * inv_det

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
        from maths.vector4d import Vector4d

        if type(other) == int or type(other) == float:
            obj = Matrix44()
            for col in range(4):
                self[col] -= other
            return obj
        elif type(other) == Matrix44:
            obj = Matrix44()

            if inline_math_mult:
                # for j in range(0, 4):
                # for i in range(0, 4):
                # obj[i][j] = self[i][j] * other[j][j] + self[i][j] * other[j].y + self[i][j] * other[j].z + self[i][j] * other[j].w
                pass
            else:
                self_transpose = self.get_transpose()
                # self_transpose = self
                for i in range(4):
                    for j in range(4):
                        obj[j][i] = self_transpose[i].dot(other[j])
            return obj

        elif type(other) == Vector4d:
            obj = Vector4d()

            if inline_math_mult:
                for i in range(4):
                    obj[i] = self[3][i] * other.x + self[3][i] * other.y + self[3][i] * other.z + self[3][i] * other.w
            else:
                self_transpose = self.get_transpose()
                for col in range(4):
                    obj[col] = self_transpose[col].dot(other)

            return obj
        raise NotImplemented
