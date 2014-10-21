from core.differential_geometry import DifferentialGeometry
from core.texture import Texture


class ConstantTexture(Texture):

    def __init__(self, value):
        super().__init__()

        self.value = value

    def get_evaluate(self, differential_geometry: DifferentialGeometry):
        return self.value
