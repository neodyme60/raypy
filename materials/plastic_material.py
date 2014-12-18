from core.bsdf import BSDF
from core.bxdf import Microfacet, Lambertian
from core.differential_geometry import DifferentialGeometry
from core.fresnel import FresnelDielectric
from core.material import Material
from core.microfacet_distribution import Blinn
from core.texture import Texture


class PlasticMaterial(Material):

    def __init__(self, kd: Texture, ks: Texture, rough: Texture, bump: Texture):
        super().__init__()
        self.Kd = kd
        self.Ks = ks
        self.roughness = rough
        self.bumpMap = bump

    def get_bsdf(self, dgGeom: DifferentialGeometry, dgShading: DifferentialGeometry)->[BSDF]:

        dgs = DifferentialGeometry()
        if self.bumpMap is None:
            dgs = dgShading
        else:
            #todo Bump(bumpMap, dgGeom, dgShading, &dgs);
            pass

        bsdf = BSDF(dgs, dgGeom.normal)

        kd = self.Kd.get_evaluate(dgs).get_clamp()
        if not kd.get_is_black():
            diff = Lambertian(kd)
            bsdf.add(diff)

        ks = self.Ks.get_evaluate(dgs).get_clamp()
        if not ks.get_is_black():
            fresnel = FresnelDielectric(1.5, 1.0)
            rough = self.roughness.get_evaluate(dgs)
            spec = Microfacet(ks, fresnel, Blinn(1.0 / rough))
            bsdf.add(spec)

        return bsdf
