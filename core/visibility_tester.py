from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.scene import Scene
from core.spectrum import Spectrum
from maths.config import infinity_max_f
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class VisibilityTester:

    def __init__(self):
        self.ray = Ray()

    def SetSegment(self, p1: Point3d, eps1: float, p2: Point3d, eps2: float, time: float):
        dist = (p1 - p2).get_length()
        d = (p2-p1) / dist
        self.ray = Ray(p1, d, eps1, dist * (1.0 - eps2), time)
#        Assert(!r.HasNaNs())

    def SetRay(self, p: Point3d, eps: float, w: Vector3d, time: float):
        self.ray = Ray(p, w, eps, infinity_max_f, time)
 #       Assert(!r.HasNaNs());

    def Unoccluded(self, scene: Scene)->bool:
        return not scene.get_is_intersected(self.ray)

    def Transmittance(self, scene: Scene, renderer: Renderer, sample: Sample)->Spectrum:
        return renderer.Transmittance(scene, self.ray, sample)
