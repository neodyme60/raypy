from core.bbox import BoundingBox
from core.bsdf import BSDF
from core.bssrdf import BSSRDF
from core.differential_geometry import DifferentialGeometry
from core.light import AreaLight
from core.material import Material
from core.primitive import Primitive
from core.ray import Ray
from core.shape import Shape
from core.intersection import Intersection
from core.transform import Transform


class GeometricPrimitive(Primitive):
    def __init__(self, shape: Shape, material: Material):
        super().__init__()
        self.shape = shape
        self.material = material
        self.areaLight = []

    def get_can_intersect(self):
        return self.shape.get_can_intersect()

    def get_world_bound(self) -> BoundingBox:
        return self.shape.get_world_bound()

    def get_intersection(self, ray: Ray, intersection: Intersection) -> bool:
        hit, thit = self.shape.get_intersection(ray, intersection.differentialGeometry)
        if not hit:
            return False
        intersection.primitive = self
        intersection.WorldToObject = self.shape.objectToWorld
        intersection.ObjectToWorld = self.shape.objectToWorld
        ray.max_t = thit
        return True

    def get_is_intersected(self, ray: Ray) -> bool:
        return self.shape.get_is_intersected(ray)

    def get_refine(self, refined):
        shapes = []
        self.shape.get_refine(shapes)
        for i in shapes:
            refined.append(GeometricPrimitive(i, self.material))

    def GetBSDF(self, dg: DifferentialGeometry, ObjectToWorld: Transform)->BSDF:
        dgs = DifferentialGeometry()
        self.shape.get_shading_geometry(ObjectToWorld, dg, dgs)
        return self.material.get_bsdf(dg, dgs)

    def GetBSSRDF(self, dg: DifferentialGeometry, ObjectToWorld: Transform)->BSSRDF:
        dgs = DifferentialGeometry()
        self.shape.get_shading_geometry(ObjectToWorld, dg, dgs)
        return self.material.get_bssdf(dg, dgs)

    def  GetAreaLight(self)->AreaLight:
        return self.areaLight