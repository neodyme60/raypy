from core import texture
from core.differential_geometry import DifferentialGeometry
from core.material import Material
from core.texture import Texture


class MirrorMaterial(Material):

    def __init__(self, texture: Texture):
        super().__init__()
        self.kr = texture

    def get_bsdf(self, dg: DifferentialGeometry):

        #get surface albedo
        s = self.kr.get_evaluate(dg)


