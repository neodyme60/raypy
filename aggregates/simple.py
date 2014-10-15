import copy
from core.aggregate import Aggregate
from core.intersection import Intersection

class Simple(Aggregate):

    def __init__(self):
        Aggregate.__init__(self)

    def get_can_intersect(self)->bool:
        return True

    def get_intersection(self, ray, intersection)->bool:
        i = Intersection()
        has_intersection = False
        for obj in self.primitives:
            r = copy.deepcopy(ray)
            if obj.get_intersection(r, i):
                if i.ray_epsilon < intersection.ray_epsilon:
                    intersection.ray_epsilon = i.ray_epsilon
                    intersection.differentialGeometry.point = i.differentialGeometry.point
                    intersection.differentialGeometry.normal = i.differentialGeometry.normal
                    intersection.differentialGeometry.shape = i.differentialGeometry.shape
                    has_intersection = True
        return has_intersection

    def get_is_intersected(self, ray)->bool:
        for obj in self.primitives:
            if obj.get_is_intersected(ray):
                return True
        return False

