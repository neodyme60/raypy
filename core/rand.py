from numpy import random

OneMinusEpsilon=0.9999999403953552

def stratified_sample_2D(samples: [(float, float)], nx: int, ny: int, jitter: bool):
    dx = 1.0 / nx
    dy = 1.0 / ny
    for y in range(0, ny):
        for x in range(0, nx):
            if jitter == True:
                jx, jy = random.random(), random.random()
            else:
                jx = jy =0.5
            samples[x+y*nx] = (min((x + jx) * dx, OneMinusEpsilon), min((y + jy) * dy, OneMinusEpsilon))

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

