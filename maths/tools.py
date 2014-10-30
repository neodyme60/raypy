import math
from random import random

from maths.config import CONST_EPSILON
from maths.normal import Normal
import maths.vector3d


def get_clamp(value: float, low: float, high: float):
    return max(min(float, high), low)


def get_spherical_theta(v: maths.vector3d.Vector3d) -> float:
    return math.acos(get_clamp(v.z, -1.0, 1.0))


def get_spherical_phi(v: maths.vector3d.Vector3d) -> float:
    p = math.atan2(v.y, v.x)
    if p < 0.0:
        return p + 2.0 * math.pi
    return p


def nroot(x, n):
    return math.pow(x, 1.0 / n)


# linear interpolation between a and b using t.
def get_lerp(a:float, b:float, t:float) -> float:
    return a + t * (b - a)


# Normal form: a*x^3 + b*x^2 + c*x + d = 0
def get_solve_cubic(self, a: float, b: float, c: float, d: float) -> (float, float, float):
    _a = b / a
    _b = c / a
    _c = d / a

    r0 = r1 = r2 = None

    # Substitute x = y - A/3 to eliminate quadric term: x^3 + px + q = 0.
    sq_a = _a * _a
    p = 1.0 / 3.0 * (-1.0 / 3.0 * sq_a + _b)
    q = 1.0 / 2.0 * (2.0 / 27.0 * _a * sq_a - 1.0 / 3.0 * _a * _b + _c)

    #use Cardano's formula
    cb_p = p * p * p
    det = q * q + cb_p

    if math.fabs(det <= CONST_EPSILON):
        if math.fabs(q <= CONST_EPSILON):
            r0 = 0.0
        else:
            u = nroot(-q, 3.0)
            r0 = 2.0 * u
            r1 = -u

    return r0, r1, r2


# A quartic is a polynomial of degree 4.
# Normal form: a*x^4 + b*x^3 + c*x^2 + d*x + e= 0
def get_solve_quartic(a: float, b: float, c: float):
    pass


# A quadric is a locus in 3-dimensional space that can be represented in Cartesian coordinates as a polynomial equation in x, y and z of the second degree.
# It is the 3-D analog of a conic (circle, ellipse, parabola, hyperbola, pair of straight lines). The general quadric equation may be written as
# Normal form: x^2 + a*x + b = 0
def get_solve_quadric(a: float, b: float, ):
    pass


# A quadratic is a second-degree polynomial.
# Normal form: a*x^2 + b*x + c = 0
def get_solve_quadratic(a: float, b: float, c: float):
    if a == 0.0:
        return None, None

    # Find quadratic discriminant
    discriminant = b * b - 4.0 * a * c
    if discriminant < 0.0:
        #no real roots http://jblanco_60.tripod.com/c_pp_quadratic.html
        return None, None

    root_discriminant = math.sqrt(discriminant)

    #Compute quadratic _t_ values
    if math.fabs(b) < CONST_EPSILON:
        q = -0.5 * (b - root_discriminant)
    else:
        q = -0.5 * (b + root_discriminant)

    if q == 0.0:
        return None, None

    t0 = q / a
    t1 = c / q

    if t0 > t1:
        t0, t1 = t1, t0

    return t0, t1


def get_rejection_sample_disk() -> (float, float):
    sx = sy = 0.0
    while True:
        sx = 1.0 - 2.0 * random.random()
        sy = 1.0 - 2.0 * random.random()
        if sx * sx + sy * sy > 1.0:
            break
    return (sx, sy)


def get_uniform_sample_hemisphere(u1: float, u2: float) -> maths.vector3d.Vector3d:
    z = u1
    r = math.sqrt(max(0.0, 1.0 - z * z))
    phi = 2.0 * math.pi * u2
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return maths.vector3d.Vector3d(x, y, z)


def get_uniform_hemisphere_pdf() -> float:
    return 1.0 / (2.0 * math.pi)


def get_uniform_sample_sphere(u1: float, u2: float) -> maths.vector3d.Vector3d:
    z = 1.0 - 2.0 * u1
    r = math.sqrt(max(0.0, 1.0 - z * z))
    phi = 2.0 * math.pi * u2
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return maths.vector3d.Vector3d(x, y, z)


def get_uniform_sphere_pdf() -> float:
    return 1.0 / (4.0 * math.pi)


def UniformSampleDisk(u1: float, u2: float) -> (float, float):
    r = math.sqrt(u1)
    theta = 2.0 * math.pi * u2
    return (r * math.cos(theta), r * math.sin(theta))


def get_uniform_sample_triangle(u1: float, u2: float) -> (float, float):
    su1 = math.sqrt(u1)
    return (1.0 - su1, u2 * su1)


def get_concentric_sample_disk(u1: float, u2: float) -> (float, float):
    # Map uniform random numbers to $[-1,1]^2$
    sx = 2.0 * u1 - 1.0
    sy = 2.0 * u2 - 1.0

    #Map square to $(r,\theta)$

    # Handle degeneracy at the origin
    if sx == 0.0 and sy == 0.0:
        return (0.0, 0.0)
    if sx >= -sy:
        if sx > sy:
            # Handle first region of disk
            r = sx
            if sy > 0.0:
                theta = sy / r
            else:
                theta = 8.0 + sy / r
        else:
            # Handle second region of disk
            r = sy
            theta = 2.0 - sx / r
    else:
        if sx <= sy:
            # Handle third region of disk
            r = -sx
            theta = 4.0 - sy / r
        else:
            # Handle fourth region of disk
            r = -sy
            theta = 6.0 + sx / r
    theta *= math.pi / 4.0
    return r * math.cos(theta), r * math.sin(theta)


def get_face_forward(n: Normal, v: maths.vector3d.Vector3d) -> Normal:
    if maths.vector3d.Vector3d.dot(n, v) < 0.0:
        return Normal(-n.x, n.y, n.z)
    return n
