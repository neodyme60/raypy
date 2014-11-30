from random import random
import math
from maths.config import CONST_TWOPI_INV
from maths.vector3d import Vector3d

OneMinusEpsilon=0.9999999403953552

def get_radical_invers(n: int, base: int)->float:
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
def StratifiedSample1D(samp: [float], nSamples: int, jitter: bool=True):
    invTot = 1.0 / nSamples
    for i in range(nSamples):
        if jitter:
           delta = random()
        else:
            delta = 0.5
        samp[i] = min((i + delta) * invTot, OneMinusEpsilon)

def StratifiedSample2D(samp: [(float, float)], nx: int, ny: int, jitter: bool=True):
    dx = 1.0 / nx
    dy = 1.0 / ny
    for y  in range(ny):
        for x in range(nx):
            if jitter:
                jx, jy = random(), random()
            else:
                jx = jy =0.5
            samp[y*nx + x] = (min((x + jx) * dx, OneMinusEpsilon), min((y + jy) * dy, OneMinusEpsilon))

# Monte Carlo Function Definitions
def RejectionSampleDisk()->(float, float):
    sx = 0.0
    sy = 0.0
    while True:
        sx = 1.0 - 2.0 * random()
        sy = 1.0 - 2.0 * random()
        if sx*sx + sy*sy > 1.0:
            break
    return (sx,sy)

def UniformSampleHemisphere(u1: float, u2: float)->Vector3d:
    z = u1
    r = math.sqrt(max(0.0, 1.0 - z*z))
    phi = 2 *math.pi * u2
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return Vector3d(x, y, z)

def UniformHemispherePdf()->float:
    return CONST_TWOPI_INV

def UniformSampleSphere(u1: float, u2: float)->Vector3d:
    z = 1.0 - 2.0 * u1
    r = math.sqrt(max(0.0, 1.0 - z*z))
    phi = 2 *math.pi * u2
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return Vector3d(x, y, z)

def UniformSpherePdf()->float:
    return 1.0 / (4.0 * math.pi)

def UniformSampleDisk(u1: float, u2: float)->(float, float):
    r = math.sqrt(u1)
    theta = 2.0 * math.pi * u2
    return r * math.cos(theta), r * math.sin(theta)

def ConcentricSampleDisk(u1: float, u2: float)->(float, float):
    # Map uniform random numbers to $[-1,1]^2$
    sx = 2.0 * u1 - 1.0
    sy = 2.0 * u2 - 1.0

    # Map square to $(r,\theta)$

    # Handle degeneracy at the origin
    if sx == 0.0 and sy == 0.0:
        return(0.0,0.0)
    if (sx >= -sy):
        if (sx > sy):
            # Handle first region of disk
            r = sx
            if sy > 0.0:
                theta = sy/r
            else:
                theta = 8.0 + sy/r
        else:
            # Handle second region of disk
            r = sy
            theta = 2.0 - sx/r
    else:
        if sx <= sy:
            # Handle third region of disk
            r = -sx
            theta = 4.0 - sy/r
        else:
            # Handle fourth region of disk
            r = -sy
            theta = 6.0 + sx/r
    theta *= math.pi / 4.0
    return r*math.cos(theta), r*math.sin(theta)

def CosineSampleHemisphere(u1: float, u2: float)->Vector3d:
    x, y = ConcentricSampleDisk(u1, u2)
    z = math.sqrt(max(0.0, 1.0 - x*x - y*y))
    return Vector3d(x, y, z)

def BalanceHeuristic(nf: int, fPdf: float, ng: int, gPdf: float)->float:
    return (nf * fPdf) / (nf * fPdf + ng * gPdf)

def PowerHeuristic(nf: int, fPdf: float, ng: int, gPdf: float)->float:
    f = nf * fPdf
    g = ng * gPdf
    return (f*f) / (f*f + g*g)

