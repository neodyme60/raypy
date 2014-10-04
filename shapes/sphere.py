from core.bbox import BoundingBox
from core.shape import Shape
import maths
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.intersection import Intersection
from core.transform import Transform


class Sphere(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, radius: float):
        Shape.__init__(self, o2w, w2o)

        self.radius = radius
        self.radius_squared = self.radius * self.radius

    def get_intersection(self, ray, intersection: Intersection) ->bool:

        # ray from word_space_to_object_space
        ray_o = ray * self.worldToObject

        o = Vector3d.create_from_point3d(ray_o.origin)

        a = Vector3d.dot(ray_o.direction, ray_o.direction)
        b = 2.0 * Vector3d.dot(ray_o.direction, o)
        c = Vector3d.dot(o, o) - self.radius_squared

        # Solve quadratic equation for _t_ values
        t0, t1 = maths.tools.get_solve_quadratic(a, b, c)
        if t0 == None and t1 == None:
            return False

        # Compute intersection distance along ray
        if t0 > ray.max_t or t1 < ray.min_t:
            return False
        thit = t0
        if t0 < ray.min_t:
            thit = t1
        if thit > ray.max_t:
            return False

        intersection.ray_epsilon = thit
        return True

    def get_is_intersected(self, ray) -> bool:

        # ray from word_space_to_object_space
        ray_o = ray * self.worldToObject

        o = Vector3d.create_from_point3d(ray_o.origin)

        a = Vector3d.dot(ray_o.direction, ray_o.direction)
        b = 2.0 * Vector3d.dot(ray_o.direction, o)
        c = Vector3d.dot(o, o) - self.radius_squared

        # Solve quadratic equation for _t_ values
        t0, t1 = maths.tools.get_solve_quadratic(a, b, c)
        if t0 == None and t1 == None:
            return False

        # Compute intersection distance along ray
        if t0 > ray.max_t or t1 < ray.min_t:
            return False
        thit = t0
        if t0 < ray.min_t:
            thit = t1
        if thit > ray.max_t:
            return False

        return True

    def get_object_bound(self) -> BoundingBox:
        return BoundingBox(Point3d(-self.radius, -self.radius, -self.radius),
                           Point3d(self.radius, self.radius, self.radius))
