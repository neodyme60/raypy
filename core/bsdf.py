from random import random
import math
from core.bxdf import BxDF, BxDFType
from core.differential_geometry import DifferentialGeometry
from core.monte_carlo import StratifiedSample2D
from core.sample import Sample
from core.spectrum import Spectrum
from maths import vector3d
from maths.normal import Normal
from maths.tools import get_clamp
from maths.vector3d import Vector3d


class BSDF:
    def __init__(self, dg: DifferentialGeometry, ngeom: Normal):
        self.bxdfs = list()
        self.dgShading = dg
        self.ng = ngeom
        self.nn = self.dgShading.normal
        self.sn = self.dgShading.normal
        self.tn = Vector3d.cross(self.nn, self.sn)

    def add(self, other: BxDF):
        self.bxdfs.append(other)

    def WorldToLocal(self, v: Vector3d)->Vector3d:
        return Vector3d(Vector3d.dot(v, self.sn), Vector3d.dot(v, self.tn), Vector3d.dot(v, self.nn))

    def LocalToWorld(self, v: Vector3d)->Vector3d:
        return Vector3d(self.sn.x * v.x + self.tn.x * v.y + self.nn.x * v.z,
                      self.sn.y * v.x + self.tn.y * v.y + self.nn.y * v.z,
                      self.sn.z * v.x + self.tn.z * v.y + self.nn.z * v.z)

    def get_Pdf(self, wi: Vector3d, wo: Vector3d, BxDFTypeFlags:int=BxDFType.BSDF_ALL) -> float:
        if len(self.bxdfs) == 0:
            return 0.0
        pdf = 0.0
        matching_count = 0
        for bxdf in self.bxdfs:
            if bxdf.get_matches_flags(self, BxDFTypeFlags):
                matching_count += 1
                pdf += bxdf.get_Pdf(wi, wo)
        if matching_count == 0:
            return 0.0
        return pdf / float(matching_count)

    def get_bxdf_count(self, flags) -> int:
        return len(self.bxdfs)

    def get_bxdf_count_by_flag(self, flags) -> int:
        count = 0
        for bxdf in self.bxdfs:
            if bxdf.get_matches_flags(self, flags):
                count += 1
        return count

    def f(self, woW: Vector3d, wiW: Vector3d, BxDFTypeFlags: int)->Spectrum:
        wi = self.WorldToLocal(wiW)
        wo = self.WorldToLocal(woW)
        if Vector3d.dot(wiW, self.ng) * Vector3d.dot(woW, self.ng) > 0: # ignore BTDFs
            flags = BxDFTypeFlags & ~BxDFType.BSDF_TRANSMISSION
        else:  # ignore BRDFs
            flags = BxDFTypeFlags & ~BxDFType.BSDF_REFLECTION
        f = Spectrum(0.0)
        for i in range(len(self.bxdfs)):
            if self.bxdfs[i].MatchesFlags(flags):
                f += self.bxdfs[i].get_f(wo, wi)
        return f

    def rho(self, BxDFTypeFlags: int, sqrtSamples: int)->Spectrum:
        nSamples = sqrtSamples * sqrtSamples
        s1 = [(float, float)] * nSamples
        StratifiedSample2D(s1, sqrtSamples, sqrtSamples)
        s2 = [(float, float)] * nSamples
        StratifiedSample2D(s2, sqrtSamples, sqrtSamples)

        ret = Spectrum(0.0)
        for i in range(len(self.bxdfs)):
            if self.bxdfs[i].MatchesFlags(BxDFTypeFlags):
                ret += self.bxdfs[i].rho(nSamples, s1, s2)
        return ret

class BSDFSampleOffsets:
    def __init__(self, count: int, sample: Sample):
        self.nSamples = count
        self.componentOffset = sample.add_1d(self.nSamples)
        self.dirOffset = sample.add_2d(self.nSamples)


class BSDFSample:
    def __init__(self):
        self.uDir = (float, float)
        self.uComponent = float

    @staticmethod
    def create_from_floats(up0: float, up1: float, ucomp: float):
        s = BSDFSample()
        # Assert(up0 >= 0.f && up0 < 1.f);
        #        Assert(up1 >= 0.f && up1 < 1.f);
        #        Assert(ucomp >= 0.f && ucomp < 1.f);
        s.uDir = (up0, up1)
        s.uComponent = ucomp
        return s

    @staticmethod
    def create_from_random():
        s = BSDFSample()
        s.uComponent = random()
        s.uDir = (random(), random())
        return s

    @staticmethod
    def create_from_sample(sample: Sample, offsets: BSDFSampleOffsets, num: int):
        s = BSDFSample()
        # Assert(n < sample->n2D[offsets.dirOffset]);
        #Assert(n < sample->n1D[offsets.componentOffset]);
        s.uPos = sample.values_array_2d[offsets.dirOffset + num]
        s.uComponent = sample.values_array_1d[offsets.componentOffset + num]
        #Assert(uDir[0] >= 0.f && uDir[0] < 1.f);
        #Assert(uDir[1] >= 0.f && uDir[1] < 1.f);
        #Assert(uComponent >= 0.f && uComponent < 1.f);
        return s


def CosTheta(w: vector3d) -> float:
    return w.z


def AbsCosTheta(w: vector3d) -> float:
    return math.fabs(w.z)


def SinTheta2(w: vector3d) -> float:
    return max(0.0, 1.0 - CosTheta(w) * CosTheta(w))


def SinTheta(w: vector3d) -> float:
    return math.sqrt(SinTheta2(w))


def CosPhi(w: vector3d) -> float:
    sintheta = SinTheta(w)
    if sintheta == 0.0:
        return 1.0
    return get_clamp(w.x / sintheta, -1.0, 1.0)


def SinPhi(w: vector3d) -> float:
    sintheta = SinTheta(w)
    if sintheta == 0.0:
        return 0.0
    return get_clamp(w.y / sintheta, -1.0, 1.0)


def SameHemisphere(w: vector3d, wp: vector3d) -> bool:
    return w.z * wp.z > 0.0

