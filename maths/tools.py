import math


# linear interpolation between a and b using t.
from random import random
from maths.vector3d import Vector3d


def get_lerp(a:float,  b:float, t:float)->float:
  return a + t * (b-a)

def get_solve_quadratic(a: float, b: float, c: float):

    #Find quadratic discriminant
    discriminant = b * b - 4.0 * a *  c
    if discriminant < 0.0:
        return None, None

    root_discriminant = math.sqrt(discriminant)

    #Compute quadratic _t_ values
    if b < 0:
        q = -0.5 * (b - root_discriminant)
    else:
        q = -0.5 * (b + root_discriminant)

    t0 = q / a
    t1 = c / q

    if t0 > t1:
        t0, t1 = t1, t0

    return t0, t1

def get_rejection_sample_disk()->(float, float):
    sx = sy = 0.0
    while True:
        sx = 1.0 - 2.0 * random.random()
        sy = 1.0 - 2.0 * random.random()
        if sx*sx + sy*sy > 1.0:
            break
    return (sx, sy)

def get_uniform_sample_hemisphere(u1: float, u2: float)->Vector3d:
    z = u1
    r = math.sqrt(max(0.0, 1.0 - z*z))
    phi = 2.0 * math.pi * u2
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return Vector3d(x, y, z)

def get_uniform_hemisphere_pdf()->float:
    return 1.0 / (2.0 * math.pi)

def get_uniform_sample_sphere(u1: float, u2: float)->Vector3d:
    z = 1.0 - 2.0 * u1
    r = math.sqrt(max(0.0, 1.0 - z*z))
    phi = 2.0 * math.pi * u2
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return Vector3d(x, y, z)

def get_uniform_sphere_pdf()->float:
    return 1.0 / (4.0 * math.pi)

def UniformSampleDisk(u1: float, u2: float)->(float,float):
    r = math.sqrt(u1)
    theta = 2.0 * math.pi * u2
    return  (r * math.cos(theta), r * math.sin(theta))

def get_uniform_sample_triangle(u1: float, u2: float)->(float, float):
    su1 = math.sqrt(u1)
    return (1.0 - su1, u2 * su1)


def get_concentric_sample_disk(u1: float, u2: float)->(float, float):
    #Map uniform random numbers to $[-1,1]^2$
    sx = 2.0 * u1 - 1.0
    sy = 2.0 * u2 - 1.0

    #Map square to $(r,\theta)$

    # Handle degeneracy at the origin
    if sx == 0.0 and sy == 0.0:
        return(0.0, 0.0)
    if sx >= -sy:
        if sx > sy:
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
    return (r * math.cos(theta), r * math.sin(theta))
