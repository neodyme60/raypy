from core.transform import Transform

__author__ = 'nicolas'

class Primitive:

    def __init__(self):
        self.transform = Transform(Transform.create_identity(), Transform.create_identity())

    def CanIntersect(self)->bool:
        raise Exception("must be implemented")

    def Intersect(self, ray, intersection)->bool:
        raise Exception("must be implemented")

    def IntersectP(self, ray)->bool:
        raise Exception("must be implemented")
