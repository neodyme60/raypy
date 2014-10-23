import random
import math
from core.buckets import BucketOrderInfo, BucketExtend
from core.rand import get_radical_invers
from core.sample import Sample
from core.sampler import Sampler
import maths.tools



class HaltonSampler(Sampler):
    def __init__(self, bucket_extend: BucketExtend, samples_per_pixel: int, shutter_open: float, shutter_close: float):
        super().__init__(bucket_extend, samples_per_pixel, shutter_open, shutter_close)

        self.pos_x = self.bucket_extend.start_x
        self.pos_y = self.bucket_extend.start_y
        self.image_samples = [(float, float)] * self.samples_per_pixel
        self.lens_samples = [(float, float)] * self.samples_per_pixel
        self.time_samples = [float] * self.samples_per_pixel

        delta = max(self.bucket_extend.get_width(), self.bucket_extend.get_height())
        self.wantedSamples = self.samples_per_pixel * delta * delta
        self.currentSample = 0

    def get_more_samples(self) ->  [Sample]:

        if self.currentSample >= self.wantedSamples:
            return 0

        samples = []
        sample = Sample()

        # generate random tuple for image samples and shift them
        while True:
            u = get_radical_invers(self.currentSample, 3)
            v = get_radical_invers(self.currentSample, 2)
            lerp_delta = float(max(self.bucket_extend.get_width(), self.bucket_extend.get_height()))
            image_xy = (maths.tools.get_lerp(self.bucket_extend.start_x, self.bucket_extend.start_x + lerp_delta, u),
                        maths.tools.get_lerp(self.bucket_extend.start_y, self.bucket_extend.start_y + lerp_delta, v))
            self.currentSample = self.currentSample+1
            if image_xy[0] < self.bucket_extend.end_x and image_xy[1] < self.bucket_extend.end_y:
                sample.image_xy = image_xy
                break

        sample.lens_uv = (get_radical_invers(self.currentSample, 5), get_radical_invers(self.currentSample, 7))
        sample.time = maths.tools.get_lerp(self.shutter_open, self.shutter_close, get_radical_invers(self.currentSample, 11))

        samples.append(sample)

        return samples

    def get_sub_sampler(self, bucket_index: int, bucket_order_info: BucketOrderInfo):

        bucket_extend = self.compute_sub_window(bucket_index, bucket_order_info)

        if bucket_extend.get_is_null():
            return None

        return HaltonSampler(bucket_extend, self.samples_per_pixel, self.shutter_open, self.shutter_close)

    def get_round_size(self, size: int) -> int:
        return 1

    def get_maximum_sample_count(self) -> int:
        return 1