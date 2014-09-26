import random
import math
from core.buckets import BucketOrderInfo
from core.sample import Sample
from core.sampler import Sampler
import maths.tools


class RandomSampler(Sampler):
    def __init__(self, start_x: int, end_x: int, start_y: int, end_y: int, samples_count: int, shutter_open: float,
                 shutter_close: float):

        Sampler.__init__(self, start_x, end_x, start_y, end_y, samples_count, shutter_open, shutter_close)
        self.samples_count = samples_count
        self.pos_x = self.pixel_start_x
        self.pos_y = self.pixel_start_y
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

    def get_more_samples(self, sample: Sample) -> int:

        # no more random value
        if self.sample_pos == self.samples_count:
            if self.pixel_start_x == self.pixel_end_x or self.pixel_start_y == self.pixel_end_y:
                return False

            self.pos_x += 1

            if self.pos_x == self.pixel_end_x:
                self.pos_x = self.pixel_start_x
                self.pos_y += 1

            if self.pos_y == self.pixel_end_y:
                return False

            # re compute random values and reset counter
            self.internal_fill_random(self.samples_count)
            self.sample_pos = 0

        sample.image_x = self.image_samples[2 * self.sample_pos]
        sample.image_y = self.image_samples[2 * self.sample_pos + 1]
        sample.lens_u = self.lens_samples[2 * self.sample_pos]
        sample.lens_v = self.lens_samples[2 * self.sample_pos + 1]
        sample.time = maths.tools.get_lerp(self.time_samples[self.sample_pos], self.shutter_open, self.shutter_close)

        self.sample_pos += 1

        return True

    def get_sub_sampler(self, bucket_index: int, bucket_order_info: BucketOrderInfo):

        xo = bucket_index % bucket_order_info.width
        yo = bucket_index // bucket_order_info.height

        tx0 = float(xo) / float(bucket_order_info.width)
        ty0 = float(yo) / float(bucket_order_info.height)

        tx1 = float(xo + 1) / float(bucket_order_info.width)
        ty1 = float(yo + 1) / float(bucket_order_info.height)

        start_x = int(math.floor(maths.tools.get_lerp(self.pixel_start_x, self.pixel_end_x, tx0)))
        start_y = int(math.floor(maths.tools.get_lerp(self.pixel_start_y, self.pixel_end_y, ty0)))

        end_x = int(math.floor(maths.tools.get_lerp(self.pixel_start_x, self.pixel_end_x, tx1)))
        end_y = int(math.floor(maths.tools.get_lerp(self.pixel_start_y, self.pixel_end_y, ty1)))

        return RandomSampler(start_x, end_x, start_y, end_y, self.samples_count, self.shutter_open, self.shutter_close)

    def get_round_size(self, size: int) -> int:
        return 1

    def get_Maximum_Sample_Count(self) -> int:
        return 1