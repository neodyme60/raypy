import math


# linear interpolation between a and b using t.
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