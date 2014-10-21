from core.differential_geometry import DifferentialGeometry


class Texture:
    def __init__(self):
        pass

    def get_evaluate(self, differential_geometry: DifferentialGeometry):
        raise NotImplemented
