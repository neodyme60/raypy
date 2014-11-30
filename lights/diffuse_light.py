from core.light import Light
from core.spectrum import Spectrum
from core.transform import Transform
from maths.point3d import Point3d

class DiffuseLight(Light):

    def __init__(self, l2w: Transform, s: Spectrum):
        super().__init__(l2w)
        self.point = Point3d(0.0, 0.0, 0.0)
        self.intensity = Spectrum()

