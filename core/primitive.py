from core.transform import Transform

__author__ = 'nicolas'

class Primitive:

    def __init__(self):
        self.transform = Transform(Transform.create_identity(), Transform.create_identity())

    def get_can_intersect(self)->bool:
        raise Exception("must be implemented")

    def get_intersection(self, ray, intersection)->bool:
        raise Exception("must be implemented")

    def get_is_intersected(self, ray)->bool:
        raise Exception("must be implemented")
