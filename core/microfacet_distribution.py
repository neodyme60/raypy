import math
from maths.config import CONST_PI, CONST_INV_TWOPI
from maths.tools import SphericalDirection1
from maths.vector3d import Vector3d


class MicrofacetDistribution:
    # MicrofacetDistribution Interface
    def __init__(self):
        pass

    def D(self, wh: Vector3d) -> float:
        raise NotImplemented

    def Sample_f(self, wo: Vector3d, u: (float, float)) -> (Vector3d, float):
        raise NotImplemented

    def Pdf(self, wo: Vector3d, wi: Vector3d) -> float:
        raise NotImplemented


class Blinn(MicrofacetDistribution):
    def __init__(self, e: float):
        super().__init__()
        if e > 10000.0 or math.isnan(e):
            e = 10000.0
        self.exponent = e

    def D(self, wh: Vector3d) -> float:
        from core.bxdf import AbsCosTheta

        costhetah = AbsCosTheta(wh)
        return (self.exponent + 2) * CONST_INV_TWOPI * math.pow(costhetah, self.exponent)

    def Sample_f(self, wo: Vector3d, u: (float, float)) -> (Vector3d, float):
        from core.bxdf import SameHemisphere
        # Compute sampled half-angle vector $\wh$ for Blinn distribution
        costheta = math.pow(u[0], 1.0 / (self.exponent + 1))
        sintheta = math.sqrt(max(0.0, 1.0 - costheta * costheta))
        phi = u[1] * 2.0 * CONST_PI
        wh = SphericalDirection1(sintheta, costheta, phi)
        if not SameHemisphere(wo, wh):
            wh = -wh

        # Compute incident direction by reflecting about $\wh$
        uu = wh * Vector3d.dot(wo, wh)
        wi = -wo + (uu * 2.0)

        # Compute PDF for $\wi$ from Blinn distribution
        blinn_pdf = ((self.exponent + 1.0) * math.pow(costheta, self.exponent)) / (
            2.0 * CONST_PI * 4.0 * Vector3d.dot(wo, wh))
        if Vector3d.dot(wo, wh) <= 0.0:
            blinn_pdf = 0.0
        return wi, blinn_pdf

    def Pdf(self, wo: Vector3d, wi: Vector3d) -> float:
        from core.bxdf import AbsCosTheta

        wh = (wo + wi).get_normalized()
        costheta = AbsCosTheta(wh)
        # Compute PDF for $\wi$ from Blinn distribution
        blinn_pdf = ((self.exponent + 1.0) * math.pow(costheta, self.exponent)) / (
            2.0 * CONST_PI * 4.0 * Vector3d.dot(wo, wh))
        if Vector3d.dot(wo, wh) <= 0.0:
            blinn_pdf = 0.0
        return blinn_pdf
