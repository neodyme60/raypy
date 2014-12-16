from core.light_sample import LightSample
from core.ray import Ray
from core.scene import Scene
from core.spectrum import Spectrum
from core.transform import Transform
from core.visibility_tester import VisibilityTester
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class Light:
    def __init__(self, l2w: Transform, samples_count: int=1):
        self.lightToWorld = l2w
        self.worldToObject = l2w.get_invert()
        self.samples_count = max(1, samples_count)

    def get_power(self, scene) -> Spectrum:
        raise NotImplemented

    # return wi / spectrum / pdf
    #todo epsilon param
    def Sample_L1(self, p: Point3d, ls: LightSample, time: float, vis: VisibilityTester) -> (Vector3d, Spectrum, float):
        raise NotImplemented

    #return ray / normal /  spectrum / pdf
    def Sample_L2(self, scene: Scene, ls: LightSample, u: (float, float), n: Normal, r: Ray, time: float) -> (Spectrum, float):
        raise NotImplemented

    def get_is_delta_light(self):
        raise NotImplemented

    def Le(self, r: Ray) -> Spectrum:
        return Spectrum(0.0)

    def get_pdf(self, p: Point3d, wi: Vector3d) -> float:
        pass


class AreaLight(Light):

    def __init__(self, l2w: Transform, ns: int):
        super().__init__(l2w, ns)

    def L(self, p: Point3d, n: Normal, w: Vector3d)->Spectrum:
        raise NotImplemented

