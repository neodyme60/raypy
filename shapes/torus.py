from core.bbox import BoundingBox
from core.differential_geometry import DifferentialGeometry
from core.ray import Ray
from core.shape import Shape
from core.transform import Transform


class Torus(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, radius: float):
        super().__init__(o2w, w2o)

    def get_can_intersect(self):
        return True

    def get_intersection(self, ray: Ray, dg: DifferentialGeometry) -> (bool, float):
        #todo
        raise NotImplemented

    def get_is_intersected(self, ray) -> bool:
        #todo
        raise NotImplemented

    def get_object_bound(self) -> BoundingBox:
        return None
