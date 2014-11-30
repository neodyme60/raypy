from core.aggregate import Aggregate
from core.intersection import Intersection
from core.primitive import Primitive
from maths.config import infinity_max_f


class Simple(Aggregate):

    def __init__(self, primitives: [Primitive]):
        super().__init__()
        self.primitives = primitives
        self.allCanIntersect = False

        # Initialize _primitives_ with primitives for grid
        primitives_new = []
        for p in primitives:
            p.get_fully_refine(primitives_new)
        self.primitives = primitives_new

    def get_can_intersect(self)->bool:
        return True

    def get_intersection(self, ray, intersection)->bool:
        i = Intersection()
        has_intersection = False
        t = infinity_max_f
        for obj in self.primitives:
            if obj.get_intersection(ray, i):
                if ray.max_t < t:
                    intersection.ray_epsilon = i.ray_epsilon
                    intersection.differentialGeometry.point = i.differentialGeometry.point
                    intersection.differentialGeometry.normal = i.differentialGeometry.normal
                    intersection.differentialGeometry.shape = i.differentialGeometry.shape
                    intersection.primitive = obj
                    t = ray.max_t
                    has_intersection = True

        return has_intersection

    def get_is_intersected(self, ray)->bool:
        for obj in self.primitives:
            if obj.get_is_intersected(ray):
                return True
        return False

