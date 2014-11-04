from core.bbox import BoundingBox
from core.shape import Shape
import maths
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.intersection import Intersection
from core.transform import Transform
from core.ray import Ray
from maths.vector4d import Vector4d


class Sphere(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, radius: float, zmin: float, zmax: float, phimax: float):
        super().__init__(o2w, w2o)

        self.radius = radius
        self.zmin = zmin
        self.zmax = zmax
        self.phimax = phimax
        self.radius_squared = self.radius * self.radius

    def get_can_intersect(self):
        return True

    def internal_solve(self, ray_l: Ray, ray_w: Ray) -> (float, float):

        o = Vector3d.create_from_point3d(ray_l.origin)

        a = Vector3d.dot(ray_l.direction, ray_l.direction)
        b = 2.0 * Vector3d.dot(ray_l.direction, o)
        c = Vector3d.dot(o, o) - self.radius_squared

        # Solve quadratic equation for _t_ values
        t0, t1 = maths.tools.get_solve_quadratic(a, b, c)
        if t0 == None and t1 == None:
            return (None, None)

        # Compute intersection distance along ray
        if t0 > ray_w.max_t or t1 < ray_w.min_t:
            return (None, None)

        thit = t0
        if t0 < ray_w.min_t:
            thit = t1
        if thit > ray_w.max_t:
            return (None, None)
        return t0, t1

    def get_intersection(self, ray: Ray, intersection: Intersection) -> bool:

        # ray from word_space_to_object_space
        ray_o = ray * self.worldToObject

        t0, t1 = self.internal_solve(ray_o, ray)

        if t0 == None and t1 == None:
            return False

        if ray_o.min_t <= t0 < ray_o.max_t:
            intersection.ray_epsilon = t0
            intersection.differentialGeometry.point = ray_o.get_at(intersection.ray_epsilon) * self.objectToWorld
            # intersection.differentialGeometry.point = ray.get_at(intersection.ray_epsilon)
            # * self.objectToWorld
            # intersection.differentialGeometry.normal = Normal.create_from_point3d(intersection.differentialGeometry.point);

            v = Vector4d(intersection.differentialGeometry.point.x,
                         intersection.differentialGeometry.point.y,
                         intersection.differentialGeometry.point.z,
                         1.0)* self.worldToObject
            v = Vector3d(v.x, v.y, v.z).get_normalized()
            intersection.differentialGeometry.normal = Normal(v.x, v.y, v.z) * self.objectToWorld
            intersection.differentialGeometry.shape = self
            return True
        return False

    def get_is_intersected(self, ray: Ray) -> bool:

        # ray from world_space_to_object_space
        ray_o = ray * self.worldToObject

        t0, t1 = self.internal_solve(ray_o, ray)

        return t0 != None and t1 != None

    def get_object_bound(self) -> BoundingBox:
        return BoundingBox(Point3d(-self.radius, -self.radius, -self.radius),
                           Point3d(self.radius, self.radius, self.radius))
