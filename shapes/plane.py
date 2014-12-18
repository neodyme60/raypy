import math
from core.bbox import BoundingBox
from core.differential_geometry import DifferentialGeometry
from core.intersection import Intersection
from core.shape import Shape
from maths.config import CONST_EPSILON
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.ray import Ray


class Plane(Shape):
    # plan in form ax+by+cz+d=0

    def __init__(self, o2w, w2o):
        super().__init__(o2w, w2o)

        self.normal = Vector3d.get_up()
        self.distance = 0.0

    def get_can_intersect(self):
        return True

    def get_object_bound(self) -> BoundingBox:
        return BoundingBox(Point3d(-5.0, -0.1, -5.0), Point3d(5.0, 0.1, 5.0))

    def get_intersection(self, ray: Ray, dg: DifferentialGeometry) -> (bool, float):

        # ray from word_space_to_object_space
        ray_o = ray * self.worldToObject

        denominator = Vector3d.dot(self.normal, ray_o.direction)
        if math.fabs(denominator) < CONST_EPSILON:
            return False, 0.0

        o = Vector3d.create_from_point3d(ray_o.origin)

        t = -(Vector3d.dot(self.normal, o) + self.distance) / denominator
        if ray_o.min_t <= t < ray_o.max_t:
            dg.point = ray_o.get_at(t) * self.objectToWorld
            dg.normal = self.normal  * self.objectToWorld
            dg.shape = self
            return True, t
        return False, 0.0

    def get_is_intersected(self, ray) -> bool:
        # ray from word_space_to_object_space
        ray_o = ray * self.worldToObject

        denominator = Vector3d.dot(self.normal, ray_o.direction)
        if math.fabs(denominator) < CONST_EPSILON:
            return False

        o = Vector3d.create_from_point3d(ray_o.origin)

        t = -(Vector3d.dot(self.normal, o) + self.distance) / denominator
        if ray_o.min_t <= t < ray_o.max_t:
            return True

        return False
