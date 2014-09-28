from core.buckets import BucketExtend
from core.sampler import Sampler


class StratifiedSampler(Sampler):
    def __init__(self, bucket_extend: BucketExtend, samples_count: int, shutter_open: float, shutter_close: float):

        Sampler.__init__(self, bucket_extend, samples_count, shutter_open, shutter_close)
        self.samples_count = samples_count
        self.pos_x = self.pixel_start_x
        self.pos_y = self.pixel_start_y
        self.image_samples = [float, float] * samples_count
        self.lens_samples = [float, float] * samples_count
        self.time_samples = [float] * samples_count
        self.sample_pos = 0
