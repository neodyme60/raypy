from enum import Enum
import string

from core.integrator import SurfaceIntegrator
from core.intersection import Intersection
from core.param_set import ParamSet
from core.ray import Ray
from core.scene import Scene



class LightStrategy(Enum):
    SAMPLE_ALL_UNIFORM = 0
    SAMPLE_ONE_UNIFORM = 1

class DirectLightingIntegrator(SurfaceIntegrator):

    def __init__(self, samples_count: int, max_distance: float, max_depth: int = 1, lightStrategy: LightStrategy = LightStrategy.SAMPLE_ONE_UNIFORM):
        super().__init__()
        self.samples_count = samples_count
        self.max_distance = max_distance
        self.light_strategiy = lightStrategy
        self.max_depth = max_depth


    def Li(self, scene: Scene, ray: Ray, intersection: Intersection):
        pass