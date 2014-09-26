from maths.vector3d import Vector3d
import math

#based on http://www.cs.stanford.edu/~acoates/quaternion.h

class Quaternion:
    __slots__ = ['x', 'y', 'z', 'w']

    def __init__(self, x: float=0.0, y: float=0.0, z: float=0.0, w: float=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @staticmethod
    def create_from_vector4d(other):
        return Quaternion(other.x, other.y, other.z, other.w)

    @staticmethod
    def create_from_vector3d(other: Vector3d, w: float=0.0):
        return Quaternion(other.x, other.y, other.z, w)

    def get_complex(self) -> Vector3d:
        return Vector3d(self.x, self.y, self.z)

    def get_real(self) -> float:
        return self.w

    #
    # @brief Returns the norm ("magnitude") of the quaternion.
    # @return The 2-norm of [ w(), x(), y(), z() ]<sup>T</sup>.
    #
    def get_norm(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w)

    def get_conjugate(self):
        return Quaternion.create_from_vector3d(-self.get_complex(), self.get_real())

    def __div__(self, other):
        if type(float):
            d_inv = 1.0 / other
            return Quaternion(self.x * d_inv, self.y * d_inv, self.z * d_inv, self.w * d_inv)

    def __sub__(self, other):
        if type(Quaternion):
            return Quaternion(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, other):
        if type(float):
            return Quaternion(self.x * other, self.y * other, self.z * other, self.w * other)
        elif type(Quaternion):
            return Quaternion(self.y * other.z - self.z * other.y + self.x * other.w + self.w * other.x,
                              self.z * other.x - self.x * other.z + self.y * other.w + self.w * other.y,
                              self.x * other.y - self.y * other.x + self.z * other.w + self.w * other.z,
                              self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z)

    # Unary operator
    def __neg__(self):
        return Quaternion(-self.x, -self.y, -self.z, -self.w)

    # brief Computes the inverse of this quaternion.
    #
    #note This is a general inverse.  If you know a priori
    # that you're using a unit quaternion (i.e., norm() == 1),
    # it will be significantly faster to use conjugate() instead.
    #
    # return The quaternion q such that q * (*this) == (*this) * q
    # == [ 0 0 0 1 ]<sup>T</sup>.
    def get_inverse(self):
        return self.get_conjugate() / self.get_norm()


