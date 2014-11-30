import string
from core.light import Light
from core.spectrum import Spectrum
from core.transform import Transform
from maths.point3d import Point3d

class ProjectionLight(Light):

    def __init__(self, l2w: Transform, s: Spectrum, texname: string, fov: float):
        super().__init__(l2w)
        self.point = Point3d(0.0, 0.0, 0.0)
        self.intensity = Spectrum()
