from aggregates.simple import Simple
from core.integrator import SurfaceIntegrator
from core.intersection import Intersection
from core.ray import Ray


class Scene():

    def __init__(self, surface_integrator: SurfaceIntegrator):
        self.aggregate = Simple()
        self.surface_integrator = surface_integrator

    def add_geometry(self, other):
        self.aggregate.add(other)

    def get_intersection(self, ray: Ray, intersection: Intersection):
        if self.aggregate.get_is_intersected(ray):
            return self.aggregate.get_intersection(ray, intersection)
        return False

    def get_is_intersected(self, ray: Ray):
        return self.aggregate.get_is_intersected(ray)
