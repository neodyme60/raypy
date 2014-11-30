from core.bsdf import BSDF
from core.differential_geometry import DifferentialGeometry
from core.material import Material
from core.texture import Texture
from maths.tools import get_clamp


class MirrorMaterial(Material):

    def __init__(self, r: Texture, bump: Texture= None):
        super().__init__()
        self.Kr = r
        self.bumpMap = bump

    def get_bsdf(self, dgGeom: DifferentialGeometry, dgShading: DifferentialGeometry)->[BSDF]:

        dgs = DifferentialGeometry()
        if self.bumpMap == None:
            dgs = dgShading
        else:
            #todo Bump(bumpMap, dgGeom, dgShading, &dgs);
            pass

        bsdf = BSDF(dgs, dgGeom.normal)

        r = self.Kr.get_evaluate(dgs).get_clamp()

        if not r.get_is_black():
            bsdf.add(SpecularReflection(r))

        return bsdf

