from core.material import Material
from core.texture import Texture


class KdSubsurfaceMaterial(Material):

    def __init__(self, kd: Texture, kr: Texture, mfp: Texture, e: Texture, bump: Texture):
        super().__init__()

