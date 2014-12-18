from core.material import Material
from core.texture import Texture


class MetalMaterial(Material):

    def __init__(self, eta: Texture, k: Texture, rough: Texture, bump: Texture):
        super().__init__()
