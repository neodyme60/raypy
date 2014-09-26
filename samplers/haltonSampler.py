from core.sampler import Sampler


class HaltonSampler(Sampler):
    def __init__(self, start_x:int, end_x:int, start_y:int, end_y:int, nb_samples:int, sopen:float, sclose:float):
        Sampler.__init__(self, start_x, end_x, end_y, nb_samples, sopen, sclose)

