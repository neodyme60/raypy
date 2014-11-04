from core.bbox import BoundingBox
from core.material import Material
from core.primitive import Primitive
from core.ray import Ray
from core.shape import Shape
from core.intersection import Intersection

class GeometricPrimitive(Primitive):

    def __init__(self, shape: Shape, material: Material):
        super().__init__()
        self.shape = shape
        self.material = material

    def get_can_intersect(self):
        return self.shape.get_world_bound()

    def get_world_bound(self)->BoundingBox:
       return self.shape.get_world_bound()

    def get_intersection(self, ray: Ray, intersection: Intersection)->bool:
       return self.get_intersection(ray, intersection)

    def get_is_intersected(self, ray: Ray)->bool:
       return self.get_is_intersected(ray)

    def get_refine(self, refined):
        shapes = []
        self.shape.get_refine(shapes)
        for i in shapes:
            refined.append(GeometricPrimitive(i, self.material))
