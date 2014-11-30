import random

from core.buckets import BucketOrderInfo, BucketExtend
from core.monte_carlo import StratifiedSample2D
from core.sample import Sample
from core.sampler import Sampler
import maths.tools


class StratifiedSampler(Sampler):
    def __init__(self, bucket_extend: BucketExtend, samples_x: int, samples_y: int, jitter: bool, shutterOpen: float, shutterClose: float):
        super().__init__(bucket_extend, samples_x*samples_y, shutterOpen, shutterClose)

        self.pos_x = self.bucket_extend.start_x
        self.pos_y = self.bucket_extend.start_y
        self.image_samples = [(float, float)] * self.samples_per_pixel
        self.lens_samples = [(float, float)] * self.samples_per_pixel
        self.time_samples = [float] * self.samples_per_pixel
        self.jitter_samples = jitter

        #samples per pixels
        self.samples_x = samples_x
        self.samples_y = samples_y

        # re compute random values and reset counter1
        self.internal_fill_stratified(self.samples_per_pixel)
        self.sample_pos = 0

        self.samples_cache = [Sample()] * self.samples_per_pixel

    def internal_fill_stratified(self, nb_samples):

        # generate random tuple for image samples and shift them
        StratifiedSample2D(self.image_samples, self.samples_x, self.samples_y, self.jitter_samples)
        for i in range(nb_samples):
            self.image_samples[i] = (self.image_samples[i][0] + self.pos_x, self.image_samples[i][1] + self.pos_y)

        # generate random tuple for lens samples and shift them
        StratifiedSample2D(self.lens_samples, self.samples_x, self.samples_y, self.jitter_samples)
        for i in range(nb_samples):
            self.lens_samples[i] = (self.lens_samples[i][0], self.lens_samples[i][1])

        # generate random value for time samples
        for i in range(nb_samples):
            self.time_samples[i] = random.random()

    def get_more_samples(self) -> [Sample]:

        # move to next sample and generate random sub sample
        if self.sample_pos == (self.samples_per_pixel):

            if self.bucket_extend.get_is_null():
                return []

            self.pos_x += 1

            if self.pos_x == self.bucket_extend.end_x:
                self.pos_x = self.bucket_extend.start_x
                self.pos_y += 1

            if self.pos_y == self.bucket_extend.end_y:
                return []

            # re compute random values and reset counter
            self.internal_fill_stratified(self.samples_per_pixel)
            self.sample_pos = 0

        for i in range(self.samples_per_pixel):
            self.samples_cache[i].image_xy = self.image_samples[i]
            self.samples_cache[i].lens_uv = self.lens_samples[i]
    #todo        sample.time = maths.tools.get_lerp(self.shutter_open, self.shutter_close, self.time_samples[self.sample_pos])
            self.samples_cache[i].time = maths.tools.get_lerp(0.0, 0.0, self.time_samples[i])

        self.sample_pos += self.samples_per_pixel

        return self.samples_cache

    def get_sub_sampler(self, bucket_index: int, bucket_order_info: BucketOrderInfo):

        bucket_extend = self.compute_sub_window(bucket_index, bucket_order_info)

        if bucket_extend.get_is_null():
            return None

        return StratifiedSampler(bucket_extend, self.samples_x, self.samples_y, self.jitter_samples, self.shutterOpen, self.shutterClose)

    def get_round_size(self, size: int) -> int:
        return 1

    def get_maximum_sample_count(self) -> int:
        return self.samples_x * self.samples_y