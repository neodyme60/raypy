from core.bbox import BoundingBox
from core.transform import Transform


class Primitive:

    def __init__(self):
        self.transform = Transform(Transform.create_identity(), Transform.create_identity())

    def get_can_intersect(self)->bool:
        raise Exception("must be implemented")

    def get_intersection(self, ray, intersection)->bool:
        raise Exception("must be implemented")

    def get_is_intersected(self, ray)->bool:
        return True

    def get_bsdf(self):
        pass

    def get_world_bound(self)->BoundingBox:
        raise NotImplemented

    def get_refine(self, primitives_list):
        raise Exception("must be implemented")

    def get_fully_refine(self, primitives_list):
        todo = [self]
        while len(todo)>0:
            prim = todo.pop()
            if prim.get_can_intersect():
                primitives_list.append(prim)
            else:
                prim.get_refine(todo)
