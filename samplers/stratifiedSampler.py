import random

from core.buckets import BucketOrderInfo, BucketExtend
from core.rand import stratified_sample_2D
from core.sample import Sample
from core.sampler import Sampler
import maths.tools


class StratifiedSampler(Sampler):
    def __init__(self, bucket_extend: BucketExtend, samples_x: int, samples_y: int, jitter: bool):
        super().__init__(bucket_extend, samples_x*samples_y)

        self.pos_x = self.bucket_extend.start_x
        self.pos_y = self.bucket_extend.start_y
        self.image_samples = [(float, float)] * self.samples_per_pixel
        self.lens_samples = [(float, float)] * self.samples_per_pixel
        self.time_samples = [float] * self.samples_per_pixel
        self.jitter_samples = jitter

        #samples per pixels
        self.samples_x = samples_x
        self.samples_y = samples_y

        self.sample_pos = 0

        # re compute random values and reset counter
        self.internal_fill_stratified(self.samples_per_pixel)

    def internal_fill_stratified(self, nb_samples):

        # generate random tuple for image samples and shift them
        stratified_sample_2D(self.image_samples, self.samples_x, self.samples_y, self.jitter_samples)
        for i in range(nb_samples):
            self.image_samples[i] = (self.image_samples[i][0] + self.pos_x, self.image_samples[i][1] + self.pos_y)

        # generate random tuple for lens samples and shift them
        stratified_sample_2D(self.lens_samples, self.samples_x, self.samples_y, self.jitter_samples)
        for i in range(nb_samples):
            self.lens_samples[i] = (self.lens_samples[i][0] + self.pos_x, self.lens_samples[i][1] + self.pos_y)

        # generate random value for time samples
        for i in range(nb_samples):
            self.time_samples[i] = random.random()

    def get_more_samples(self) -> [Sample]:

        samples= []

        # move to next sample and generate random sub sample
        if self.sample_pos == (self.samples_per_pixel):

            if self.bucket_extend.get_is_null():
                return 0

            self.pos_x += 1

            if self.pos_x == self.bucket_extend.end_x:
                self.pos_x = self.bucket_extend.start_x
                self.pos_y += 1

            if self.pos_y == self.bucket_extend.end_y:
                return 0

            # re compute random values and reset counter
            self.internal_fill_stratified(self.samples_per_pixel)
            self.sample_pos = 0

        sample = Sample()
        sample.image_xy = self.image_samples[self.sample_pos]
        sample.lens_uv = self.lens_samples[self.sample_pos]
        sample.time = maths.tools.get_lerp(self.shutter_open, self.shutter_close, self.time_samples[self.sample_pos])

        samples.append(sample)

        self.sample_pos += 1

        return samples

    def get_sub_sampler(self, bucket_index: int, bucket_order_info: BucketOrderInfo):

        bucket_extend = self.compute_sub_window(bucket_index, bucket_order_info)

        if bucket_extend.get_is_null():
            return None

        return StratifiedSampler(bucket_extend, self.samples_x, self.samples_y, self.jitter_samples, self.shutter_open, self.shutter_close)

    def get_round_size(self, size: int) -> int:
        return 1

    def get_maximum_sample_count(self) -> int:
        return self.samples_x * self.samples_y