from core.bsdf import BSDF
from core.differential_geometry import DifferentialGeometry


class Material:

    def __init__(self):
        pass

    def get_bsdf(self, dg: DifferentialGeometry, dgShading: DifferentialGeometry)->[BSDF]:
        raise NotImplemented

    def get_bssdf(self, dg: DifferentialGeometry, dgShading: DifferentialGeometry):
        return None

