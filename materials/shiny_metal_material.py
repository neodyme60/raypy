from core.material import Material
from core.texture import Texture


class ShinyMetalMaterial(Material):

    def __init__(self, r: Texture, bump: Texture= None):
        super().__init__()