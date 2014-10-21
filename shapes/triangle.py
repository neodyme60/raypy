from core.bbox import BoundingBox
from core.shape import Shape
import maths
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.intersection import Intersection
from core.transform import Transform


class Triangle(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, radius: float):
        super().__init__(o2w, w2o)

    def get_intersection(self, ray, intersection: Intersection) ->bool:
        #todo
        raise NotImplemented

    def get_is_intersected(self, ray) -> bool:
        #todo
        raise NotImplemented

    def get_object_bound(self) -> BoundingBox:
        return BoundingBox(Point3d(-self.radius, -self.radius, -self.radius),
                           Point3d(self.radius, self.radius, self.radius))
