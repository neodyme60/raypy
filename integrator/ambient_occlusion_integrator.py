from random import random
from core.integrator import SurfaceIntegrator
from core.intersection import Intersection
from core.ray import Ray
from core.scene import Scene
from core.spectrum import Spectrum
import maths.tools
from maths.vector3d import Vector3d


class AmbientOcclusionIntegrator(SurfaceIntegrator):

    def __init__(self, samples_count: int, max_distance: float):
        super().__init__()
        self.samples_count = samples_count
        self.max_distance = max_distance

    def Li(self, scene: Scene, ray: Ray, intersection: Intersection)->Spectrum:

        occlusion = 0

        for i in range(self.samples_count):
            w = maths.tools.get_uniform_sample_sphere(random(), random())

            n = maths.tools.get_face_forward(intersection.differentialGeometry.normal, -ray.direction)

            if Vector3d.dot(w, n) < 0.0:
                w = -w

            r = Ray(intersection.differentialGeometry.point, w, 0.01, self.max_distance)
            if scene.get_is_intersected(r):
                occlusion += 1

        return Spectrum(1.0-(float(occlusion) / float(self.samples_count)))
