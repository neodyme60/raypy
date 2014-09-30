from core.bbox import BoundingBox
from core.intersection import Intersection
from core.ray import Ray
from maths.normal import Normal
from maths.point3d import Point3d


class Shape:

    def __init__(self, o2w, w2o):
        self.objectToWorld = o2w
        self.worldToObject = w2o

    def get_can_intersect(self)->bool:
        raise Exception("must be implemented")

    def get_intersection(self, ray:Ray)->Intersection:
        raise Exception("must be implemented")

    def get_is_intersected(self, ray:Ray)->bool:
        raise Exception("must be implemented")

    def get_object_bound(self)->BoundingBox:
        raise Exception("must be implemented")

    def get_world_object_bound(self)->BoundingBox:
        raise Exception("must be implemented")

    def get_are(self)->float:
        raise Exception("must be implemented")

    def get_sample(u1:float, u2:float)->(Point3d, Normal):
        raise Exception("must be implemented")

