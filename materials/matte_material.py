from core.bsdf import BSDF
from core.bxdf import Lambertian, OrenNayar
from core.differential_geometry import DifferentialGeometry
from core.material import Material
from core.texture import Texture
from maths.tools import get_clamp


class MatteMaterial(Material):

    def __init__(self, kd: Texture, sig: Texture, bump: Texture= None):
        super().__init__()
        self.Kd = kd
        self.sigma = sig
        self.bumpMap = bump

    def get_bsdf(self, dgGeom: DifferentialGeometry, dgShading: DifferentialGeometry)->[BSDF]:

        dgs = DifferentialGeometry()
        if self.bumpMap == None:
            dgs = dgShading
        else:
            #todo Bump(bumpMap, dgGeom, dgShading, &dgs);
            pass

        bsdf = BSDF(dgs, dgGeom.normal)

        r = self.Kd.get_evaluate(dgs).get_clamp()
        sig = get_clamp(self.sigma.get_evaluate(dgs), 0.0, 90.0)

        if r.get_is_black():
            bsdf.add(OrenNayar(r,sig))
        else:
            bsdf.add(Lambertian(r))

        return bsdf

    def get_bssdf(self, dg: DifferentialGeometry, dgShading: DifferentialGeometry):
        return None


