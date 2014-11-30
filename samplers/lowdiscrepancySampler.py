from core.buckets import BucketExtend
from core.sampler import Sampler


class LowDiscrepancySampler(Sampler):
    def __init__(self, bucket_extend: BucketExtend, samples_count: int, shutterOpen: float, shutterClose: float):
        super().__init__(bucket_extend, samples_count, shutterOpen, shutterClose)

        self.samples_count = samples_count
        self.pos_x = self.bucket_extend.start_x
        self.pos_y = self.bucket_extend.start_y
        self.image_samples = [float, float] * samples_count
        self.lens_samples = [float, float] * samples_count
        self.time_samples = [float] * samples_count
        self.sample_pos = 0
