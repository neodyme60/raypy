from core.intersection import Intersection
from core.ray import Ray
from core.renderer import Renderer
from core.scene import Scene
from core.spectrum import Spectrum


class Integrator():

    def __init__(self):
        pass

class SurfaceIntegrator(Integrator):

    def __init__(self):
        Integrator.__init__()

    def Li(self, scene: Scene, renderer: Renderer, ray: Ray, intersection: Intersection)->Spectrum:
        raise NotImplemented