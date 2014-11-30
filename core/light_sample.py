from random import random
from core.light_sample_offsets import LightSampleOffsets
from core.sample import Sample


class LightSample:
    def __init__(self):
        self.uPos = (float, float)
        self.uComponent = float

    @staticmethod
    def create_from_sample(sample: Sample, offsets: LightSampleOffsets, num: int):
        s = LightSample()
        # Assert(n < sample->n2D[offsets.posOffset]);
        #        Assert(n < sample->n1D[offsets.componentOffset]);
        s.uPos = sample.values_array_2d[offsets.posOffset + num]
        s.uComponent = sample.values_array_1d[offsets.componentOffset + num]
        #        Assert(uPos[0] >= 0.f && uPos[0] < 1.f);
        #        Assert(uPos[1] >= 0.f && uPos[1] < 1.f);
        #        Assert(uComponent >= 0.f && uComponent < 1.f);
        return s

    @staticmethod
    def create_from_random():
        s = LightSample()
        s.uComponent = random()
        s.uPos = (random(), random())
        return s

    @staticmethod
    def create_from_floats(up0: float, up1: float, ucomp: float):
        s = LightSample()
        # Assert(up0 >= 0.f && up0 < 1.f);
        #       Assert(up1 >= 0.f && up1 < 1.f);
        #       Assert(ucomp >= 0.f && ucomp < 1.f);
        s.uPos = (up0, up1)
        s.uComponent = ucomp
        return s
