from core.material import Material
from core.texture import Texture


class SubstrateMaterial(Material):

    def __init__(self, kd: Texture, ks: Texture, u: Texture, v: Texture, bump: Texture):
        super().__init__()
