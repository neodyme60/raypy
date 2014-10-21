from core.bxdf import BxDF, BxDFType
from maths.vector3d import Vector3d


class BSDF:
    def __init__(self):
        self.bxdfs = list()

    def add(self, other: BxDF):
        self.bxdfs.append(other)

    def get_Pdf(self, wi: Vector3d, wo: Vector3d, flags:BxDFType=BxDFType.BSDF_ALL) -> float:
        if len(self.bxdfs) == 0:
            return 0.0
        pdf = 0.0
        matching_count = 0
        for bxdf in self.bxdfs:
            if bxdf.get_matches_flags(self, flags):
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