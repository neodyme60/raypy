from core.primitive import Primitive

__author__ = 'nicolas'

class Aggregate(Primitive):

    def __init__(self):
        self.primitives = []

    def add(self, other):
        if isinstance(other, Primitive):
            self.primitives.append(other)

    def CanIntersect(self)->bool:
        return True

    def Intersect(self, ray, intersection)->bool:
        for p in self.primitives:
            pass

    def IntersectP(self, ray)->bool:
        for p in self.primitives:
            pass
