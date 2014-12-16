import math
from core.bbox import BoundingBox
from core.differential_geometry import DifferentialGeometry
from core.ray import Ray
from core.transform import Transform
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class Shape:

    def __init__(self, o2w, w2o):
        self.objectToWorld = o2w
        self.worldToObject = w2o

    def get_can_intersect(self)->bool:
        raise Exception("must be implemented")

    def get_intersection(self, ray: Ray, dg: DifferentialGeometry)->(bool, float):
        return True

    def get_is_intersected(self, ray:Ray)->bool:
        raise Exception("must be implemented")

    def get_object_bound(self)->BoundingBox:
        raise Exception("must be implemented")

    def get_world_bound(self)->BoundingBox:
        return self.objectToWorld*self.get_object_bound()

    def get_sample(self, u1:float, u2:float)->(Point3d, Normal):
        raise Exception("must be implemented")

    def get_refine(self, shapes_list):
        raise Exception("must be implemented")

    def get_shading_geometry(self, obj2world: Transform, dg: DifferentialGeometry, dgShading: DifferentialGeometry):
        dgShading.normal = dg.normal
        dgShading.point = dg.point
        dgShading.shape = dg.shape

    def Area(self):
        return 0.0

    def Pdf1(self, p: Point3d)->float:
        return 1.0 / self.Area()

    def Sample1(self, u: (float, float), n: Normal)->Point3d:
        return Point3d()

    def Pdf2(self, p: Point3d, wi: Vector3d)->float:
        # Intersect sample ray with area light geometry
        dgLight = DifferentialGeometry()
        ray = Ray(p, wi, 1e-3)
        ray.depth = -1 # temporary hack to ignore alpha mask
        b, thit =self.get_intersection(ray, dgLight)
        if not b:
            return 0.0

        # Convert light sample weight to solid angle measure
        pdf = (p - ray.get_at(thit)).get_length_squared() / (math.fabs(Vector3d.dot(dgLight.normal, -wi) * self.Area()))
        if math.isinf(pdf):
            pdf = 0.0
        return pdf

    def Sample2(self, p: Point3d, u: (float, float), n: Normal)->Point3d:
        return self.Sample1(u, n)

