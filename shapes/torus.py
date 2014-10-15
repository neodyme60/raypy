from core.bbox import BoundingBox
from core.shape import Shape
import maths
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.intersection import Intersection
from core.transform import Transform


class Torus(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, radius: float):
        Shape.__init__(self, o2w, w2o)

    def get_intersection(self, ray, intersection: Intersection) ->bool:
        #todo
        raise NotImplemented

    def get_is_intersected(self, ray) -> bool:
        #todo
        raise NotImplemented

    def get_object_bound(self) -> BoundingBox:
        #todo
        raise NotImplemented