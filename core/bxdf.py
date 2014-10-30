from enum import Enum

from core.spectrum import Spectrum
from maths.config import CONST_PI_INV
from maths.vector3d import Vector3d


class BxDFType(Enum):
    # BSDF Declarations
    BSDF_REFLECTION = 1 << 0
    BSDF_TRANSMISSION = 1 << 1
    BSDF_DIFFUSE = 1 << 2
    BSDF_GLOSSY = 1 << 3
    BSDF_SPECULAR = 1 << 4
    BSDF_ALL_TYPES = BSDF_DIFFUSE | BSDF_GLOSSY | BSDF_SPECULAR
    BSDF_ALL_REFLECTION = BSDF_REFLECTION | BSDF_ALL_TYPES
    BSDF_ALL_TRANSMISSION = BSDF_TRANSMISSION | BSDF_ALL_TYPES,
    BSDF_ALL = BSDF_ALL_REFLECTION | BSDF_ALL_TRANSMISSION

class BxDF:
    def __init__(self, bxdf_type: BxDFType):
        self.bxdf_type = bxdf_type

    def get_Pdf(self, wi: Vector3d, wo: Vector3d) -> float:
        raise NotImplemented

    def get_matches_flags(self, flags: BxDFType) -> bool:
        return (self.bxdf_type & flags) == self.bxdf_type

    def get_f(self, wo: Vector3d, wi: Vector3d)->Spectrum:
        raise NotImplemented

class SpecularReflection(BxDF):
    def __init__(self, r: Spectrum):
        super().__init__(BxDFType.BSDF_REFLECTION | BxDFType.BSDF_SPECULAR)
        self.r = r

    def get_f(self, wo: Vector3d, wi: Vector3d)->Spectrum:
        return Spectrum(0.0)

class Lambertian(BxDF):
    def __init__(self, r: Spectrum):
        super().__init__(BxDFType.BSDF_REFLECTION | BxDFType.BSDF_DIFFUSE)
        self.r = r

    def get_f(self, wo: Vector3d, wi: Vector3d)->Spectrum:
        return self.r * CONST_PI_INV

