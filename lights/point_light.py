import math
from core.light import Light
from core.light_sample import LightSample
from core.monte_carlo import UniformSampleSphere, UniformSpherePdf
from core.ray import Ray
from core.scene import Scene
from core.spectrum import Spectrum
from core.transform import Transform
from core.visibility_tester import VisibilityTester
from maths.config import infinity_max_f
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class PointLight(Light):

    def __init__(self, l2w: Transform, s: Spectrum):
        super().__init__(l2w)
        self.intensity = s
        self.lightPos = Point3d(0.0, 0.0, 0.0)*l2w

    def get_power(self, scene: Scene)->Spectrum:
        return 4.0 * math.pi * self.intensity

    #return spectrum and pdf
    def Sample_L1(self, p: Point3d, pEpsilon: float, ls: LightSample, time: float, vis: VisibilityTester)-> (Vector3d, Spectrum, float):
        wi = (self.lightPos - p).get_normalized()
        pdf = 1.0
        vis.SetSegment(p, pEpsilon, self.lightPos, 0.0, time)
        s = self.intensity / (self.lightPos - p).get_length_squared()
        return wi, s, pdf

    def Sample_L2(self, scene: Scene, ls: LightSample, u1: float, u2: float, time: float) -> (Ray, Normal, float, Spectrum):
        ray = Ray(self.lightPos, UniformSampleSphere(ls.uPos[0], ls.uPos[1]), 0.0, infinity_max_f, time)
        Ns = Normal.create_from_vector3d(ray.direction)
        pdf = UniformSpherePdf()
        return ray, Ns, pdf, self.intensity

    def get_is_delta_light(self):
        return True

    def Le(self, r: Ray)->Spectrum:
        return Spectrum(0.0)

    def get_pdf(self, p: Point3d, wi: Vector3d)->float:
        return 0.0
