from core.bbox import BoundingBox
import math
from core.shape import Shape
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.intersection import Intersection
from core.transform import Transform


class Sphere(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, radius: float):
        Shape.__init__(self, o2w, w2o)

        self.center = Vector3d(0.0, 0.0, 0.0)
        self.radius = radius
        self.radius_squared = 1.0

    def get_intersection(self, ray) -> Intersection:
        i = None
        e = self.center - ray.origin
        a = ray.direction.dot(e)

        f = self.radius_squared - e.dot(e) + (a * a)
        if f > 0.0:
            t = a - math.sqrt(f)
            if 0.1 < t < ray.max_t:
                i = Intersection()
                i.distance = t
                i.intersection = ray.origin + ray.direction * t
                i.normal = (i.intersection - self.center).get_normalized()
        return i

    def get_object_bound(self) -> BoundingBox:
        return BoundingBox(Point3d(-self.radius, -self.radius, -self.radius),
                           Point3d(self.radius, self.radius, self.radius))
