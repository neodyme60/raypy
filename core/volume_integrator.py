from core.integrator import Integrator
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.scene import Scene
from core.spectrum import Spectrum


class VolumeIntegrator(Integrator):

    def __init__(self):
        super().__init__()

    def  Li(self, scene: Scene, renderer: Renderer, ray: Ray, sample: Sample, transmittance: Spectrum)->Spectrum:
        pass

    def Transmittance(self, scene: Scene, renderer: Renderer, ray: Ray, sample: Sample)->Spectrum:
        pass

