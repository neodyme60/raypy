import math

from core.light import AreaLight
from core.light_sample import LightSample
from core.monte_carlo import UniformSampleSphere
from core.ray import Ray
from core.scene import Scene
from core.shape import Shape
from core.shape_set import ShapeSet
from core.spectrum import Spectrum
from core.transform import Transform
from core.visibility_tester import VisibilityTester
from maths.config import infinity_max_f, CONST_INV_TWOPI
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class DiffuseAreaLight(AreaLight):
    def __init__(self, l2w: Transform, le: Spectrum, ns: int, shape: Shape):
        super().__init__(l2w, ns)
        self.shapeSet = ShapeSet(shape)
        self.area = self.shapeSet.Area()
        self.Lemit = le

    def get_pdf(self, p: Point3d, wi: Vector3d) -> float:
        return self.shapeSet.Pdf2(p, wi)

    def Le(self, r: Ray) -> Spectrum:
        return super().Le(r)

    def get_power(self, scene) -> Spectrum:
        return self.Lemit * self.area * math.pi

    def get_is_delta_light(self):
        return False

    def L(self, p: Point3d, n: Normal, w: Vector3d) -> Spectrum:
        if Vector3d.dot(n, w) > 0.0:
            return self.Lemit
        return Spectrum(0.0)

    def Sample_L1(self, p: Point3d, ls: LightSample, time: float,
                  visibility: VisibilityTester) -> (Vector3d, Spectrum, float):
        ns = Normal()
        ps = self.shapeSet.Sample1(p, ls, ns)
        wi = (ps - p).get_normalized()
        visibility.SetSegment(p, 1e-3, ps, 1e-3, time)
        return wi, self.L(ps, ns, -wi), self.shapeSet.Pdf2(p, wi)

    def Sample_L2(self, scene: Scene, ls: LightSample, u: (float, float), n: Normal, ray: Ray, time: float) -> (
            Spectrum, float):
        origin = self.shapeSet.Sample2(ls, n)
        direction = UniformSampleSphere(u)
        if Vector3d.dot(direction, n) < 0.0:
            direction *= -1.0

        ray.Set(Ray(origin, direction, 1e-3, infinity_max_f, time))

        Ls = self.L(origin, n, direction)
        pdf = self.shapeSet.Pdf1(origin) * CONST_INV_TWOPI
        return ray, Ls, pdf

