from core.integrator import Integrator, SurfaceIntegrator
from core.intersection import Intersection
from core.ray import Ray
from core.renderer import Renderer
from core.scene import Scene


class AmbientOcclusionIntegrator(SurfaceIntegrator):

    def __init__(self, samples_count: int, max_dist: float):
        SurfaceIntegrator.__init__()
        self.samples_count = samples_count
        self.max_dist = max_dist

    def Li(self, scene: Scene, renderer: Renderer, ray: Ray, intersection: Intersection):
        for i in range(0, self.samples_count):
            pass