__author__ = 'nicolas'

class Shape:

    def __init__(self, o2w, w2o):
        self.objectToWorld = o2w
        self.worldToObject = w2o

    def CanIntersect(self)->bool:
        raise Exception("must be implemented")

    def Intersect(self, ray, intersection)->bool:
        raise Exception("must be implemented")

    def IntersectP(self, ray)->bool:
        raise Exception("must be implemented")