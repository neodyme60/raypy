from random import random
from core.intersection import Intersection
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.scene import Scene
from core.spectrum import Spectrum
from core.surface_integrator import SurfaceIntegrator
from maths.config import infinity_max_f
import maths.tools
from maths.vector3d import Vector3d


class AmbientOcclusionIntegrator(SurfaceIntegrator):

    def __init__(self, samples_count: int, max_distance: float):
        super().__init__()
        self.samples_count = samples_count
        self.max_distance = max_distance

    def Li(self, scene: Scene, renderer: Renderer, ray: Ray, intersection: Intersection, sample: Sample)->Spectrum:

        occlusion = 0
        intersection.ray_epsilon = infinity_max_f

        bsdf = intersection.get_bsdf(ray)
        p = bsdf.dgShading.point

        n = maths.tools.get_face_forward(intersection.differentialGeometry.normal, -ray.direction)

        for i in range(self.samples_count):
            w = maths.tools.get_uniform_sample_sphere(random(), random())

            if Vector3d.dot(w, n) < 0.0:
                w = -w

            r = Ray(p, w, 0.01, self.max_distance)
            if scene.get_is_intersected(r):
                occlusion += 1

        return Spectrum(1.0-(float(occlusion) / float(self.samples_count)))
