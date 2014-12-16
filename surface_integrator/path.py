from copy import deepcopy
from random import random
import math
from core.bsdf import BSDFSampleOffsets, BSDFSample
from core.bxdf import BxDFType
from core.camera import Camera
from core.integrator import UniformSampleOneLight
from core.intersection import Intersection
from core.light_sample_offsets import LightSampleOffsets
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.sampler import Sampler
from core.scene import Scene
from core.spectrum import Spectrum
from core.surface_integrator import SurfaceIntegrator
from maths.vector3d import Vector3d


class PathIntegrator(SurfaceIntegrator):
    def __init__(self, max_depth: int=1):
        super().__init__()
        self.maxDepth = max_depth
        self.lightSampleOffsets = [LightSampleOffsets] * self.maxDepth
        self.lightNumOffset = [int] * self.maxDepth
        self.bsdfSampleOffsets = [BSDFSampleOffsets] * self.maxDepth
        self.pathSampleOffsets = [BSDFSampleOffsets] * self.maxDepth

    def Li(self, scene, renderer: Renderer, r: Ray, intersection: Intersection, sample: Sample) -> Spectrum:
        # Declare common path integration variables
        pathThroughput = Spectrum(1.0)
        L = Spectrum(0.0)
        ray = deepcopy(r)
        specularBounce = False
        localIsect = Intersection()
        isectp = intersection
        bounces = 0
        while True:
            # Possibly add emitted light at path vertex
            if bounces == 0 or specularBounce:
                L += pathThroughput * isectp.Le(-ray.direction)

            # Sample illumination from lights to find path contribution
            bsdf = isectp.get_bsdf(ray)
            p = bsdf.dgShading.point
            n = bsdf.dgShading.normal
            wo = -ray.direction
            if bounces < self.maxDepth:
                L += pathThroughput * UniformSampleOneLight(scene, renderer, p, n, wo, ray.time, bsdf, sample,
                                                            self.lightSampleOffsets[bounces],
                                                            self.bsdfSampleOffsets[bounces],
                                                            self.lightNumOffset[bounces])
            else:
                L += pathThroughput * UniformSampleOneLight(scene, renderer, p, n, wo, ray.time, bsdf, sample)

            # Sample BSDF to get new path direction

            # Get _outgoingBSDFSample_ for sampling new path direction
            if bounces < self.maxDepth:
                outgoingBSDFSample = BSDFSample.create_from_sample(sample, self.pathSampleOffsets[bounces], 0)
            else:
                outgoingBSDFSample = BSDFSample.create_from_random()

            wi, pdf, flags, f = bsdf.Sample_f(wo, outgoingBSDFSample, BxDFType.BSDF_ALL)
            if f.get_is_black() or pdf == 0.0:
                break

            specularBounce = (flags & BxDFType.BSDF_SPECULAR) != 0
            pathThroughput *= f * math.fabs(Vector3d.dot(wi, n)) / pdf
            ray = Ray(p, wi, 0.01, ray.max_t)

            # Possibly terminate the path
            if bounces > 3:
                continueProbability = min(0.5, pathThroughput.y())
                if random() > continueProbability:
                    break
                pathThroughput /= continueProbability

            if bounces == self.maxDepth:
                break

            # Find next vertex of path
            if not scene.get_intersection(ray, localIsect):
                if specularBounce:
                    for i in range(scene.lights.size()):
                        L += pathThroughput * scene.lights[i].get_Le(ray)
                break
            # pathThroughput *= renderer->Transmittance(scene, ray, NULL, rng, arena);
            isectp = localIsect

            bounces += 1

        return L

    def Preprocess(self, scene: Scene, camera: Camera, renderer: Renderer):
        super().Preprocess(scene, camera, renderer)

    def RequestSamples(self, sampler: Sampler, sample: Sample, scene: Scene):
        for i in range(self.maxDepth):
            self.lightSampleOffsets[i] = LightSampleOffsets(1, sample)
            self.lightNumOffset[i] = sample.add_1d(1)
            self.bsdfSampleOffsets[i] = BSDFSampleOffsets(1, sample)
            self.pathSampleOffsets[i] = BSDFSampleOffsets(1, sample)
