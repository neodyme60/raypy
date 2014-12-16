from random import random
import math

from maths.config import CONST_INV_TWOPI, CONST_TWOPI, CONST_PI
from maths.tools import get_lerp
from maths.vector3d import Vector3d


OneMinusEpsilon = 0.9999999403953552


def get_radical_invers(n: int, base: int) -> float:
    val = 0.0
    inv_base = 1.0 / base
    inv_bi = inv_base
    while n > 0:
        # Compute next digit of radical inverse
        d_i = (n % base)
        val += d_i * inv_bi
        n *= inv_base
        inv_bi *= inv_base
    return val


# Sampling Function Definitions
def StratifiedSample1D(sample: [float], nSamples: int, jitter: bool=True):
    invTot = 1.0 / nSamples
    for i in range(nSamples):
        if jitter:
            delta = random()
        else:
            delta = 0.5
        sample[i] = min((i + delta) * invTot, OneMinusEpsilon)


def StratifiedSample2D(sample: [(float, float)], nx: int, ny: int, jitter: bool=True):
    dx = 1.0 / nx
    dy = 1.0 / ny
    for y in range(ny):
        for x in range(nx):
            if jitter:
                jx, jy = random(), random()
            else:
                jx = jy = 0.5
            sample[y * nx + x] = (min((x + jx) * dx, OneMinusEpsilon), min((y + jy) * dy, OneMinusEpsilon))


# Monte Carlo Function Definitions
def RejectionSampleDisk() -> (float, float):
    sx = 0.0
    sy = 0.0
    while True:
        sx = 1.0 - 2.0 * random()
        sy = 1.0 - 2.0 * random()
        if sx * sx + sy * sy > 1.0:
            break
    return (sx, sy)


def UniformSampleHemisphere(u1: float, u2: float) -> Vector3d:
    z = u1
    r = math.sqrt(max(0.0, 1.0 - z * z))
    phi = 2 * math.pi * u2
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return Vector3d(x, y, z)


def UniformHemispherePdf() -> float:
    return CONST_INV_TWOPI


def UniformSampleSphere(u: (float, float)) -> Vector3d:
    z = 1.0 - 2.0 * u[0]
    r = math.sqrt(max(0.0, 1.0 - z * z))
    phi = 2 * math.pi * u[1]
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return Vector3d(x, y, z)


def UniformSpherePdf() -> float:
    return 1.0 / (4.0 * math.pi)


def UniformSampleDisk(u1: float, u2: float) -> (float, float):
    r = math.sqrt(u1)
    theta = 2.0 * math.pi * u2
    return r * math.cos(theta), r * math.sin(theta)


def UniformConePdf(cosThetaMax: float) -> float:
    return 1.0 / (2.0 * CONST_PI * (1.0 - cosThetaMax))


def UniformSampleCone1(u: (float, float), costhetamax: float) -> float:
    costheta = (1.0 - u[0]) + u[0] * costhetamax
    sintheta = math.sqrt(1.0 - costheta * costheta)
    phi = u[1] * 2.0 * CONST_PI
    return Vector3d(math.cos(phi) * sintheta, math.sin(phi) * sintheta, costheta)


def UniformSampleCone2(u: (float, float), costhetamax: float, x: Vector3d, y: Vector3d, z: Vector3d) -> float:
    costheta = get_lerp(costhetamax, 1.0, u[0])
    sintheta = math.sqrt(1.0 - costheta * costheta)
    phi = u[1] * 2.0 * CONST_PI
    return x * math.cos(phi) * sintheta + y * math.sin(phi) * sintheta + z * costheta


def UniformSampleTriangle(u: (float, float)) -> (float, float):
    su1 = math.sqrt(u[0])
    return 1.0 - su1, u[1] * su1


def ConcentricSampleDisk(u: (float, float)) -> (float, float):
    # Map uniform random numbers to $[-1,1]^2$
    sx = 2.0 * u[0] - 1.0
    sy = 2.0 * u[1] - 1.0

    # Map square to $(r,\theta)$

    # Handle degeneracy at the origin
    if sx == 0.0 and sy == 0.0:
        return (0.0, 0.0)
    if (sx >= -sy):
        if (sx > sy):
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


def CosineSampleHemisphere(u: (float, float)) -> Vector3d:
    x, y = ConcentricSampleDisk(u)
    z = math.sqrt(max(0.0, 1.0 - x * x - y * y))
    return Vector3d(x, y, z)


def BalanceHeuristic(nf: int, fPdf: float, ng: int, gPdf: float) -> float:
    return (nf * fPdf) / (nf * fPdf + ng * gPdf)


def PowerHeuristic(nf: int, fPdf: float, ng: int, gPdf: float) -> float:
    f = nf * fPdf
    g = ng * gPdf
    return (f * f) / (f * f + g * g)


def LatinHypercube2d(samples: [(float, float)]):
    # Generate LHS samples along diagonal
    delta = 1.0 / float(len(samples))
    for i in range(len(samples)):
        samples[i] = (min((i + (random())) * delta, OneMinusEpsilon), min((i + (random())) * delta, OneMinusEpsilon))


def LatinHypercube1d(samples: [float]):
    # Generate LHS samples along diagonal
    delta = 1.0 / float(len(samples))
    for i in range(len(samples)):
        samples[i] = min((i + (random())) * delta, OneMinusEpsilon)
    # for (uint32_t j = 0; j < nDim; ++j)
    #            samples[nDim * i + j] = min((i + (rng.RandomFloat())) * delta, OneMinusEpsilon)

    # Permute LHS samples in each dimension

# for (uint32_t i = 0; i < nDim; ++i)
#        for (uint32_t j = 0; j < nSamples; ++j
#            uint32_t other = j + (rng.RandomUInt() % (nSamples - j))
#            swap(samples[nDim * j + i], samples[nDim * other + i])

