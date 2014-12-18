from core.material import Material
from core.texture import Texture


class GlassMaterial(Material):

    def __init__(self, r: Texture, t: Texture, i: Texture, bump: Texture):
        super().__init__()
