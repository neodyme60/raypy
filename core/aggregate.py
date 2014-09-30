from core.primitive import Primitive
from core.shape import Shape

class Aggregate(Primitive):

    def __init__(self):
        self.primitives = []

    def add(self, other):
        self.primitives.append(other)

    def get_can_intersect(self)->bool:
        return True

    def get_intersection(self, ray, intersection)->bool:
        for p in self.primitives:
            pass

    def get_is_intersected(self, ray)->bool:
        for obj in self.primitives:
            a = obj.get_is_intersected(ray)
            if a == True:
                return True
        return False