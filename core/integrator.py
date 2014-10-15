from core.intersection import Intersection
from core.ray import Ray
from core.spectrum import Spectrum


class Integrator():

    def __init__(self):
        pass

class SurfaceIntegrator(Integrator):

    def __init__(self):
        Integrator.__init__(self)

    def Li(self, scene, ray: Ray, intersection: Intersection)->Spectrum:
        raise NotImplemented