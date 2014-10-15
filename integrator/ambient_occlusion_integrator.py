from random import random
from core.integrator import SurfaceIntegrator
from core.intersection import Intersection
from core.ray import Ray
from core.renderer import Renderer
from core.scene import Scene
import maths.tools
from maths.vector3d import Vector3d


class AmbientOcclusionIntegrator(SurfaceIntegrator):

    def __init__(self, samples_count: int, max_distance: float):
        SurfaceIntegrator.__init__(self)
        self.samples_count = samples_count
        self.max_distance = max_distance

    def Li(self, scene: Scene, ray: Ray, intersection: Intersection):

        occlusion = 0

        for i in range(self.samples_count):
            w = maths.tools.get_uniform_sample_hemisphere(random(), random())

            if Vector3d.dot(w, intersection.differentialGeometry.normal) < 0.0:
                w = -w

            r = Ray(intersection.differentialGeometry.point, w, 0.01, self.max_distance)
            if scene.get_is_intersected(r):
                    occlusion += 0
            else:
                    occlusion += 1

        occlusion = min((float(occlusion) / float(self.samples_count)) * 255, 255)
        color = 0xff000000 + occlusion + (occlusion * 256) + (occlusion * 256 * 256)
        return color