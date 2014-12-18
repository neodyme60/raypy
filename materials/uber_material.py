from core.material import Material
from core.texture import Texture


class UberMaterial(Material):

    def __init__(self, kd: Texture, ks: Texture, kr: Texture, kt: Texture, rough: Texture, op: Texture, e: Texture, bump: Texture):
        super().__init__()