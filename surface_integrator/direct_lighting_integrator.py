from enum import Enum
from core.bsdf import BSDFSampleOffsets
from core.integrator import UniformSampleAllLights, UniformSampleOneLight
from core.intersection import Intersection
from core.light_sample_offsets import LightSampleOffsets
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.sampler import Sampler
from core.scene import Scene
from core.spectrum import Spectrum
from core.surface_integrator import SurfaceIntegrator


class LightStrategy(Enum):
    SAMPLE_ALL_UNIFORM = 0
    SAMPLE_ONE_UNIFORM = 1


class DirectLightingIntegrator(SurfaceIntegrator):
    def __init__(self, samples_count: int, max_distance: float, max_depth: int=1,
                 lightStrategy: LightStrategy=LightStrategy.SAMPLE_ONE_UNIFORM):
        super().__init__()
        self.samples_count = samples_count
        self.max_distance = max_distance
        self.light_strategy = lightStrategy
        self.max_depth = max_depth
        self.strategy = LightStrategy.SAMPLE_ALL_UNIFORM
        self.lightSampleOffsets = []
        self.bsdfSampleOffsets = []
        self.lightNumOffset = -1

    def Li(self, scene: Scene, renderer: Renderer, ray: Ray, intersection: Intersection, sample: Sample) -> Spectrum:
        L = Spectrum(0.0)
        wo = -ray.direction

        bsdf = intersection.get_bsdf(ray)

        # Compute emitted light if ray hit an area light source
        L += intersection.Le(wo)

        if len(scene.lights) > 0:
            if self.strategy == LightStrategy.SAMPLE_ALL_UNIFORM:
                L += UniformSampleAllLights(scene, renderer, intersection.differentialGeometry.point,
                                            intersection.differentialGeometry.normal, wo,
                                            ray.time, bsdf, sample, self.lightSampleOffsets, self.bsdfSampleOffsets)
            elif self.strategy == LightStrategy.SAMPLE_ONE_UNIFORM:
                L += UniformSampleOneLight(scene, renderer, intersection.differentialGeometry.point,
                                           intersection.differentialGeometry.normal, wo,
                                           ray.time, bsdf, sample, self.lightSampleOffsets, self.bsdfSampleOffsets,
                                           self.lightNumOffset)
        return L

    def RequestSamples(self, sampler: Sampler, sample: Sample, scene: Scene):

        if self.strategy == LightStrategy.SAMPLE_ALL_UNIFORM:
            # Allocate and request samples for sampling all lights
            nLights = len(scene.lights)
            self.lightSampleOffsets = [LightSampleOffsets] * nLights
            self.bsdfSampleOffsets = [BSDFSampleOffsets] * nLights
            for i in range(nLights):
                light = scene.lights[i]
                nSamples = light.samples_count
                # if (sampler)
                #                    nSamples = sampler->RoundSize(nSamples);
                self.lightSampleOffsets[i] = LightSampleOffsets(nSamples, sample)
                self.bsdfSampleOffsets[i] = BSDFSampleOffsets(nSamples, sample)
            self.lightNumOffset = -1
        else:
            # Allocate and request samples for sampling one light
            self.lightSampleOffsets = [LightSampleOffsets] * 1
            self.lightSampleOffsets[0] = LightSampleOffsets(1, sample)
            self.lightNumOffset = sample.add_1d(1)
            self.bsdfSampleOffsets = [BSDFSampleOffsets] * 1
            self.bsdfSampleOffsets[0] = BSDFSampleOffsets(1, sample)
