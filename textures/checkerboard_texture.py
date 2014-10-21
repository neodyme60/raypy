import math
from core.differential_geometry import DifferentialGeometry
from core.texture import Texture
from core.texture_mapping import TextureMapping2D


class Checkerboard2DTexture(Texture):

    def __init__(self, m: TextureMapping2D, c1: Texture, c2: Texture):
        super().__init__()

        self.mapping = m
        self.tex1 = c1
        self.tex2 = c2

    def get_evaluate(self, dg: DifferentialGeometry):

        s, t, dsdx, dtdx, dsdy, dtdy = self.mapping.get_map(dg)

        if (int(math.floor(s) + int(math.floor(t)))) % 2 == 0:
            return self.tex1.get_evaluate(dg)

        return self.tex2.get_evaluate(dg)

