import core.integrator
from core.intersection import Intersection
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.spectrum import Spectrum


class SurfaceIntegrator(core.integrator.Integrator):

    def __init__(self):
        super().__init__()

    def Li(self, scene, renderer: Renderer, ray: Ray, intersection: Intersection, sample: Sample)->Spectrum:
        raise NotImplemented