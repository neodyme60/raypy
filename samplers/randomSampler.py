import random
import math
from core.buckets import BucketOrderInfo, BucketExtend
from core.sample import Sample
from core.sampler import Sampler
import maths.tools


class RandomSampler(Sampler):
    def __init__(self, bucket_extend: BucketExtend, samples_count: int, shutter_open: float, shutter_close: float):

        Sampler.__init__(self, bucket_extend, samples_count, shutter_open, shutter_close)
        self.samples_count = samples_count
        self.pos_x = self.bucket_extend.start_x
        self.pos_y = self.bucket_extend.start_y
        self.image_samples = [float, float] * samples_count
        self.lens_samples = [float, float] * samples_count
        self.time_samples = [float] * samples_count

        # re compute random values and reset counter
        self.internal_fill_random(self.samples_count)
        self.sample_pos = 0

    def internal_fill_random(self, nb_samples):

        # generate random tuple for image samples and shift them
        for i in range(nb_samples):
            self.image_samples[i] = [random.random() + self.pos_x, random.random() + self.pos_y]

        # generate random tuple for lens samples and shift them
        for i in range(nb_samples):
            self.lens_samples[i] = [random.random() + self.pos_x, random.random() + self.pos_y]

        #generate random value for time samples
        for i in range(nb_samples):
            self.time_samples[i] = random.random()

    def get_more_samples(self, sample_list: Sample) -> int:

        #move to next sample and generate random sub sample
        if self.sample_pos == self.samples_count:

            if self.bucket_extend.get_is_null():
                return 0

            self.pos_x += 1

            if self.pos_x == self.bucket_extend.end_x:
                self.pos_x = self.bucket_extend.start_x
                self.pos_y += 1

            if self.pos_y == self.bucket_extend.end_y:
                return 0

            # re compute random values and reset counter
            self.internal_fill_random(self.samples_count)
            self.sample_pos = 0

        #we have only one sample
        sample_list[0].image_xy = self.image_samples[self.sample_pos]
        sample_list[0].lens_uv = self.lens_samples[self.sample_pos]
        sample_list[0].time = maths.tools.get_lerp(self.time_samples[self.sample_pos], self.shutter_open, self.shutter_close)

        self.sample_pos += 1

        return 1

    def get_sub_sampler(self, bucket_index: int, bucket_order_info: BucketOrderInfo):

        bucket_extend = self.compute_sub_window(bucket_index, bucket_order_info)

        if bucket_extend.get_is_null():
            return None

        return RandomSampler(bucket_extend, self.samples_count, self.shutter_open, self.shutter_close)

    def get_round_size(self, size: int) -> int:
        return 1

    def get_maximum_sample_count(self) -> int:
        return 1