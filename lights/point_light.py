import math
from core.light import Light
from core.scene import Scene
from core.spectrum import Spectrum
from core.transform import Transform
from maths.point3d import Point3d


class PointLight(Light):

    def __init__(self, l2w: Transform, s: Spectrum):
        super().__init__(l2w)
        self.point = Point3d(0.0, 0.0, 0.0)
        self.intensity = Spectrum()

    def get_power(self, scene: Scene)->Spectrum:
        return 4.0 * math.pi * self.intensity
