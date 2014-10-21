from core.differential_geometry import DifferentialGeometry


class Material:

    def __init__(self):
        pass

    def get_bsdf(self, dg: DifferentialGeometry):
        raise NotImplemented

