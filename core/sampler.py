import math

from core.buckets import BucketOrderInfo, BucketExtend
from maths.tools import get_lerp


class Sampler:
    def __init__(self, bucket_extend: BucketExtend, samples_per_pixel: int, shutterOpen: float, shutterClose: float):
        self.bucket_extend = bucket_extend
        self.samples_per_pixel = samples_per_pixel
        self.shutterOpen = shutterOpen
        self.shutterClose = shutterClose

    #return [Sample]
    def get_more_samples(self, samples) -> int:
        raise NotImplementedError

    def get_sub_sampler(self, num: int, bucket_order_info: BucketOrderInfo):
        raise NotImplementedError

    def get_round_size(self, size: int) -> int:
        raise NotImplementedError

    def get_maximum_sample_count(self) -> int:
        raise NotImplementedError

    def compute_sub_window(self, bucket_index: int, bucket_order_info: BucketOrderInfo)->BucketExtend:

        xo = bucket_index % bucket_order_info.width
        yo = bucket_index // bucket_order_info.height

        tx0 = float(xo) / float(bucket_order_info.width)
        ty0 = float(yo) / float(bucket_order_info.height)

        tx1 = float(xo + 1) / float(bucket_order_info.width)
        ty1 = float(yo + 1) / float(bucket_order_info.height)

        start_x = int(math.floor(get_lerp(self.bucket_extend.start_x, self.bucket_extend.end_x, tx0)))
        start_y = int(math.floor(get_lerp(self.bucket_extend.start_y, self.bucket_extend.end_y, ty0)))

        end_x = int(math.floor(get_lerp(self.bucket_extend.start_x, self.bucket_extend.end_x, tx1)))
        end_y = int(math.floor(get_lerp(self.bucket_extend.start_y, self.bucket_extend.end_y, ty1)))

        return BucketExtend(start_x, start_y, end_x, end_y)