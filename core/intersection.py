from core.differential_geometry import DifferentialGeometry
from maths.config import infinity_max_f


class Intersection:
    def __init__(self):
        self.primitive = None
        self.objectToWorld = None
        self.worldToObject = None
        self.ray_epsilon = infinity_max_f
        self.shape_id = 0
        self.primitive_id = 0
        self.differentialGeometry = DifferentialGeometry()


    def get_bsdf(self):
        pass