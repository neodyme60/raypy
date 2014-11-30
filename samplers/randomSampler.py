import random

from core.buckets import BucketOrderInfo, BucketExtend
from core.sample import Sample
from core.sampler import Sampler
import maths.tools


class RandomSampler(Sampler):
    def __init__(self, bucket_extend: BucketExtend, samples_per_pixel: int, shutterOpen: float, shutterClose: float):
        super().__init__(bucket_extend, samples_per_pixel, shutterOpen, shutterClose)

        self.pos_x = self.bucket_extend.start_x
        self.pos_y = self.bucket_extend.start_y
        self.image_samples = [(float, float)] * self.samples_per_pixel
        self.lens_samples = [(float, float)] * self.samples_per_pixel
        self.time_samples = [float] * self.samples_per_pixel

        # re compute random values and reset counter1
        self.internal_fill_random(self.samples_per_pixel)
        self.sample_pos = 0

    def internal_fill_random(self, nb_samples):

        # generate random tuple for image samples and shift them
        for i in range(nb_samples):
            self.image_samples[i] = (random.random() + self.pos_x, random.random() + self.pos_y)
#            self.image_samples[i] = (self.pos_x, self.pos_y)

        # generate random tuple for lens samples and shift them
        for i in range(nb_samples):
            self.lens_samples[i] = (random.random(), random.random())

        # generate random value for time samples
        for i in range(nb_samples):
            self.time_samples[i] = random.random()

    def get_more_samples(self, samples: [Sample]) -> int:

        # move to next sample and generate random sub sample
        if self.sample_pos == self.samples_per_pixel:

            if self.bucket_extend.get_is_null():
                return 0

            self.pos_x += 1

            if self.pos_x == self.bucket_extend.end_x:
                self.pos_x = self.bucket_extend.start_x
                self.pos_y += 1

            if self.pos_y == self.bucket_extend.end_y:
                return 0

            # re compute random values and reset counter
            self.internal_fill_random(self.samples_per_pixel)
            self.sample_pos = 0

        s = samples[0]
        s.image_xy = self.image_samples[self.sample_pos]
        s.lens_uv = self.lens_samples[self.sample_pos]
#todo        sample.time = maths.tools.get_lerp(self.shutter_open, self.shutter_close, self.time_samples[self.sample_pos])
        s.time = maths.tools.get_lerp(0.0, 0.0, self.time_samples[self.sample_pos])

       # Generate stratified samples for integrators
        for i in range(0, len(s.values_array_1d)):
            for j in range(0, len(s.values_array_1d[i])):
                s.values_array_1d[i][j] = random.random()

        for i in range(0, len(s.values_array_2d)):
            for j in range(0, len(s.values_array_2d[i])):
                s.values_array_2d[i][j] = (random.random(), random.random())

        self.sample_pos += 1

        return 1

    def get_sub_sampler(self, bucket_index: int, bucket_order_info: BucketOrderInfo):

        bucket_extend = self.compute_sub_window(bucket_index, bucket_order_info)

        if bucket_extend.get_is_null():
            return None

        return RandomSampler(bucket_extend, self.samples_per_pixel, self.shutterOpen, self.shutterClose)

    def get_round_size(self, size: int) -> int:
        return 1

    def get_maximum_sample_count(self) -> int:
        return 1