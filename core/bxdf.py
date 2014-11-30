import math
import core.bsdf
from core.fresnel import Fresnel
from core.monte_carlo import CosineSampleHemisphere

from core.spectrum import Spectrum
from maths.config import CONST_PI_INV
from maths.tools import get_to_radians, get_clamp
from maths.vector3d import Vector3d


# BSDF Inline Functions
def CosTheta(w: Vector3d)->float:
    return w.z

def AbsCosTheta(w: Vector3d)->float:
    return math.fabs(w.z)

def SinTheta2(w: Vector3d)->float:
    return max(0.0, 1.0 - CosTheta(w)*CosTheta(w))

def SinTheta(w: Vector3d)->float:
    return math.sqrt(SinTheta2(w))

def CosPhi(w: Vector3d)->float:
    sintheta = SinTheta(w)
    if sintheta == 0.0:
        return 1.0
    return get_clamp(w.x / sintheta, -1.0, 1.0)

def  SinPhi(w: Vector3d)->float:
    sintheta = SinTheta(w)
    if sintheta == 0.0:
        return 0.0
    return get_clamp(w.y / sintheta, -1.0, 1.0)

def SameHemisphere(w: Vector3d, wp: Vector3d)->bool:
    return w.z * wp.z > 0.0

class BxDFType:
    # BSDF Declarations
    BSDF_REFLECTION = 1 << 0
    BSDF_TRANSMISSION = 1 << 1
    BSDF_DIFFUSE = 1 << 2
    BSDF_GLOSSY = 1 << 3
    BSDF_SPECULAR = 1 << 4
    BSDF_ALL_TYPES = BSDF_DIFFUSE | BSDF_GLOSSY | BSDF_SPECULAR
    BSDF_ALL_REFLECTION = BSDF_REFLECTION | BSDF_ALL_TYPES
    BSDF_ALL_TRANSMISSION = BSDF_TRANSMISSION | BSDF_ALL_TYPES
    BSDF_ALL = BSDF_ALL_REFLECTION | BSDF_ALL_TRANSMISSION


class BxDF:
    def __init__(self, BxDFTypeFlags: int):
        self.bxdf_types = BxDFTypeFlags

    def MatchesFlags(self, BxDFTypeFlags: int )->bool:
        return (self.bxdf_types & BxDFTypeFlags) == self.bxdf_types

    def get_Pdf(self, wi: Vector3d, wo: Vector3d) -> float:
        if SameHemisphere(wo, wi):
            pdf = AbsCosTheta(wi) * CONST_PI_INV
        else:
            pdf = 0.0
        return pdf

    def get_matches_flags(self, BxDFTypeFlags: int ) -> bool:
        return (self.bxdf_types & BxDFTypeFlags) == self.bxdf_types

    def get_f(self, wo: Vector3d, wi: Vector3d)->Spectrum:
        raise NotImplemented

    def Sample_f(self, wo: Vector3d, wi: Vector3d, u1: float, u2: float)->(Vector3d, float, Spectrum):
        # Cosine-sample the hemisphere, flipping the direction if necessary
        wi = CosineSampleHemisphere(u1, u2)
        if wo.z < 0.0:
            wi.z *= -1.0
        pdf = self.get_Pdf(wo, wi)
        return wi, pdf, self.get_f(wo, wi)


class Lambertian(BxDF):
    def __init__(self, reflection_spectrum: Spectrum):
        super().__init__(BxDFType.BSDF_REFLECTION | BxDFType.BSDF_DIFFUSE)
        self.reflection_spectrum = reflection_spectrum

    def get_f(self, wo: Vector3d, wi: Vector3d)->Spectrum:
        return self.reflection_spectrum * CONST_PI_INV

class OrenNayar(BxDF):
    def __init__(self, reflection_spectrum: Spectrum, sig: float):
        super().__init__(BxDFType.BSDF_REFLECTION | BxDFType.BSDF_DIFFUSE)
        self.reflection_spectrum = reflection_spectrum
        sigma = get_to_radians(sig)
        sigma2 = sigma*sigma
        self.A = 1.0 - (sigma2 / (2.0 * (sigma2 + 0.33)))
        self.B = 0.45 * sigma2 / (sigma2 + 0.09)

    def get_f(self, wo: Vector3d, wi: Vector3d)->Spectrum:
        sinthetai = core.bsdf.SinTheta(wi)
        sinthetao = core.bsdf.SinTheta(wo)
        # Compute cosine term of Oren-Nayar model
        maxcos = 0.0
        if sinthetai > 1e-4 and sinthetao > 1e-4:
            sinphii = core.bsdf.SinPhi(wi)
            cosphii = core.bsdf.CosPhi(wi)
            sinphio = core.bsdf.SinPhi(wo)
            cosphio = core.bsdf.CosPhi(wo)
            dcos = cosphii * cosphio + sinphii * sinphio
            maxcos = max(0.0, dcos)

        # Compute sine and tangent terms of Oren-Nayar model
        if core.bsdf.AbsCosTheta(wi) > core.bsdf.AbsCosTheta(wo):
            sinalpha = sinthetao
            tanbeta = sinthetai / core.bsdf.AbsCosTheta(wi)
        else:
            sinalpha = sinthetai
            tanbeta = sinthetao / core.bsdf.AbsCosTheta(wo)

        return self.reflection_spectrum * CONST_PI_INV * (self.A + self.B * maxcos * sinalpha * tanbeta)

class SpecularReflection(BxDF):
    # SpecularReflection Public Methods
    def __init__(self, reflection_spectrum: Spectrum, f: Fresnel):
        super().__init__(BxDFType.BSDF_REFLECTION | BxDFType.BSDF_SPECULAR)
        self.reflection_spectrum = reflection_spectrum
        self.fresnel = f

    def get_f(self, wo: Vector3d, wi: Vector3d)->Spectrum:
        return Spectrum(0.0)

    def get_Pdf(self, wi: Vector3d, wo: Vector3d) -> float:
        return 0.0

    def Sample_f(self, wo: Vector3d, wi: Vector3d, u1: float, u2: float)->(Vector3d, float, Spectrum):
        # Compute perfect specular reflection direction
        wi = Vector3d(-wo.x, -wo.y, wo.z)
        pdf = 1.0
        s = self.fresnel.Evaluate(CosTheta(wo)) * self.reflection_spectrum / AbsCosTheta(*wi)
        return wi, pdf, s



