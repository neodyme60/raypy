from core.material import Material
from core.texture import Texture


class SubsurfaceMaterial(Material):

    def __init__(self, sc: float, kr: Texture, sa: Texture, sps: Texture, e: Texture, bump: Texture):
        super().__init__()
