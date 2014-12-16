from core.camera_sample import CameraSample
import core.sampler
from core.scene import Scene


class Sample(CameraSample):
    def __init__(self, sampler: core.sampler.Sampler, surface_integrator, volume_integrator, scene: Scene):
        super().__init__()

        self.values_array_1d = [[float]]
        self.values_array_2d = [[(float, float)]]
        self.internal_alloc_samples()

        if surface_integrator is not None:
            surface_integrator.RequestSamples(sampler, self, scene)

        if volume_integrator is not None:
            volume_integrator.RequestSamples(sampler, self, scene)

    def internal_alloc_samples(self):
        pass

    def add_1d(self, num:int) -> int:
        self.values_array_1d.append([float] * num)
        return len(self.values_array_1d) - 1

    def add_2d(self, num:int) -> int:
        self.values_array_2d.append([(float, float)] * num)
        return len(self.values_array_2d) - 1

    def duplicate(self, count: int):
        # todo
        pass

# s = [Sample] * count
#        for i in range(count):
#            s[i].index_values_array_1d = list(self.index_values_array_1d )
#            s[i].index_values_array_2d = list(self.index_values_array_2d )
#            s[i].values_array_1d = list(self.values_array_1d )
#            s[i].values_array_2d = list(self.values_array_2d )
#        return s
