from core.differential_geometry import DifferentialGeometry
from core.material import Material
from core.texture import Texture


class MatteMaterial(Material):

    def __init__(self, texture: Texture):
        super().__init__()

    def get_bsdf(self, dg: DifferentialGeometry):
        pass



