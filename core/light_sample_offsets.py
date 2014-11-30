from core.sample import Sample


class LightSampleOffsets:
    def __init__(self, count: int, sample: Sample):
        self.nSamples = count
        self.componentOffset = sample.add_1d(self.nSamples)
        self.posOffset = sample.add_2d(self.nSamples)

