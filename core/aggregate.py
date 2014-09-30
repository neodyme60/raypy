from core.primitive import Primitive
from core.shape import Shape

class Aggregate(Primitive):

    def __init__(self):
        self.primitives = []

    def add(self, other):
        self.primitives.append(other)

    def CanIntersect(self)->bool:
        return True

    def Intersect(self, ray, intersection)->bool:
        for p in self.primitives:
            pass

    def IntersectP(self, ray)->bool:
        if len(self.primitives) > 0:
            a = self.primitives[0].get_intersectP(ray)
            return a
        return False