from core.sampler import Sampler


class StratifiedSampler(Sampler):
    def __init__(self, start_x:int, end_x:int, start_y:int, end_y:int, nb_samples:int, sopen:float, sclose:float):
        Sampler.__init__(self, start_x, end_x, end_y, nb_samples, sopen, sclose)
        self.nb_samples = nb_samples
        self.x_pos = self.pixel_start_x
        self.y_pos = self.pixel_start_y
