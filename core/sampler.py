from core.buckets import BucketOrderInfo


class Sampler:
    def __init__(self, start_x: int, end_x: int, start_y: int, end_y: int, samples_per_pixel: int, shutter_open: float, shutter_close: float):
        self.pixel_start_x = start_x
        self.pixel_end_x = end_x
        self.pixel_start_y = start_y
        self.pixel_end_y = end_y
        self.samples_per_pixel = samples_per_pixel
        self.shutter_open = shutter_open
        self.shutter_close = shutter_close

    def get_more_samples(self, sample) -> int:
        raise NotImplementedError

    def get_sub_sampler(self, num: int, bucket_order_info: BucketOrderInfo):
        raise NotImplementedError

    def get_round_size(self, size: int) -> int:
        raise NotImplementedError

    def get_Maximum_Sample_Count(self) -> int:
        raise NotImplementedError
