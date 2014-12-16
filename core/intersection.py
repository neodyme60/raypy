import core.differential_geometry
from core.ray import Ray
from core.spectrum import Spectrum
from maths.config import infinity_max_f
from maths.vector3d import Vector3d


class Intersection:
    def __init__(self):
        self.primitive = None
        self.objectToWorld = None
        self.worldToObject = None
        self.ray_epsilon = infinity_max_f
        self.shape_id = 0
        self.primitive_id = 0
        self.differentialGeometry = core.differential_geometry.DifferentialGeometry()

    def get_bsdf(self, ray: Ray):
        # todo
        #self.differentialGeometry.ComputeDifferentials(ray)
        return self.primitive.GetBSDF(self.differentialGeometry, self.objectToWorld)

    def Le(self, w: Vector3d) -> Spectrum:
        area = self.primitive.GetAreaLight()
        if area is not None:
            return area.L(self.differentialGeometry.point, self.differentialGeometry.normal, w)
        return Spectrum(0.0)

