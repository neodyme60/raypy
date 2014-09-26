# linear interpolation between a and b using t.
def get_lerp(a:float,  b:float, t:float)->float:
  return a + t * (b-a)