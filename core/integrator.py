from core.intersection import Intersection
from core.ray import Ray
from core.spectrum import Spectrum


class Integrator():

    def __init__(self):
        pass

class SurfaceIntegrator(Integrator):

    def __init__(self):
        super().__init__()

    def Li(self, scene, ray: Ray, intersection: Intersection)->Spectrum:
        raise NotImplemented

class VolumeIntegrator(Integrator):

    def __init__(self):
        super().__init__()

