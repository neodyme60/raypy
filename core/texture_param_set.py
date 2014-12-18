from builtins import Exception
import string

from core.param_set import ParamSet
from core.spectrum import Spectrum
from maths import vector3d
from maths.normal import Normal
from maths.point3d import Point3d
from textures.constant_texture import ConstantTexture


class TextureParamSet:
    def __init__(self, geomp: ParamSet, matp: ParamSet, ft, st):
        self.geomParams = geomp
        self.materialParams = matp
        self.floatTextures = ft
        self.spectrumTextures = st

    def GetSpectrumTexture(self, n: string, d: Spectrum):
        name = self.geomParams.find_texture(n)
        if name is None:
            name = self.materialParams.find_texture(n)
        if name is not None:
            if name in self.spectrumTextures:
                return self.spectrumTextures[name]
            else:
                raise Exception("Couldn't find spectrum texture named \"%s\" for parameter \"%s\"", name)
        val = self.geomParams.find_spectrum(n, self.materialParams.find_spectrum(n, d))
        return ConstantTexture(val)

    def GetFloatTexture(self, n: string, d: float):
        name = self.geomParams.find_texture(n)
        if name is None:
            name = self.materialParams.find_texture(n)
        if name is not None:
            if name in self.floatTextures:
                return self.floatTextures[name]
            else:
                raise Exception("Couldn't find float texture named \"%s\" for parameter \"%s\"",  name)
        val = self.geomParams.find_float(n, self.materialParams.find_float(n, d))
        return ConstantTexture(val)

    def GetFloatTextureOrNull(self, name: string):
        name = self.geomParams.find_texture(name)
        if name == "":
            name = self.materialParams.find_texture(name)
        if name == "":
            return None
        if name in self.floatTextures:
            return self.floatTextures[name]
        else:
            #raise Exception("Couldn't find float texture named \"%s\" for parameter \"%s\"", name)
            return None

    def FindFloat(self, n: string, d: float) -> float:
        return self.geomParams.find_float(n, self.materialParams.find_float(n, d))

    def FindString(self, n: string, d:string="") -> string:
        return self.geomParams.find_string(n, self.materialParams.find_string(n, d))

    def FindFilename(self, n: string, d: string="") -> string:
        return self.geomParams.find_filename(n, self.materialParams.find_filename(n, d))

    def FindInt(self, n: string, d: int) -> int:
        return self.geomParams.find_int(n, self.materialParams.find_int(n, d))

    def FindBool(self, n: string, d: bool) -> bool:
        return self.geomParams.find_bool(n, self.materialParams.find_bool(n, d))

    def FindPoint(self, n: string, d: Point3d) -> Point3d:
        return self.geomParams.find_point(n, self.materialParams.find_point(n, d))

    def FindVector(self, n: string, d: vector3d) -> vector3d:
        return self.geomParams.find_vector(n, self.materialParams.find_vector(n, d))

    def FindNormal(self, n: string, d: Normal) -> Normal:
        return self.geomParams.find_normal(n, self.materialParams.find_normal(n, d))

    def FindSpectrum(self, n: string, d: Spectrum) -> Spectrum:
        return self.geomParams.find_spectrum(n, self.materialParams.find_spectrum(n, d))
