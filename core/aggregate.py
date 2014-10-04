from core.primitive import Primitive
from core.shape import Shape

class Aggregate(Primitive):

    def __init__(self):
        self.primitives = []

    def add(self, other):
        self.primitives.append(other)

    def get_can_intersect(self)->bool:
        raise NotImplemented

    def get_intersection(self, ray, intersection)->bool:
        raise NotImplemented

    def get_is_intersected(self, ray)->bool:
        raise NotImplemented