import math
from core.intersection import Intersection
from core.shape import Shape
from maths.config import CONST_EPSILON
from maths.vector3d import Vector3d
from core.ray import Ray


class Plane(Shape):
    # plan in form ax+by+cz+d=0

    def __init__(self, o2w, w2o):
        Shape.__init__(self, o2w, w2o)
        self.normal = Vector3d.get_up()
        self.distance = 0.0

    def get_intersection(self, ray: Ray, intersection: Intersection) -> bool:

        # ray from word_space_to_object_space
        ray_o = ray * self.worldToObject

        denominator = Vector3d.dot(self.normal, ray_o.direction)
        if math.fabs(denominator) < CONST_EPSILON:
            return False

        o = Vector3d.create_from_point3d(ray_o.origin)

        t = -(Vector3d.dot(self.normal, o) + self.distance) / denominator
        if 0.0 <= t < ray_o.max_t:
            intersection.ray_epsilon = t
            intersection.intersection = ray_o.origin + ray_o.direction * t
            intersection.normal = self.normal
            return True
        return False

    def get_is_intersected(self, ray) -> bool:
        denominator = Vector3d.dot(self.normal, ray.direction)
        if denominator > 1e-6:
            t = -(Vector3d.dot(self.normal, ray.origin) + self.distance) / denominator
            if 0.0 <= t < ray.max_t:
                return True
        return False