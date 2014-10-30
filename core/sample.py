from core.camera_sample import CameraSample


class Sample(CameraSample):

    def __init__(self):
        super().__init__()

        self.index_values_array_1d = []
        self.index_values_array_2d= []
        self.values_array_1d = []
        self.values_array_2d = []
        self.internal_alloc_samples()

    def internal_alloc_samples(self):
        pass

    def add_1d(self, num:int)->int:
        self.values_array_1d.append(int)
        return len(self.values_array_1d)-1

    def add_2d(self)->int:
        self.values_array_2d.append(int)
        return len(self.values_array_2d)-1

    def duplicate(self, count: int):
        s = [Sample] * count
        for i in range(count):
            s[i].index_values_array_1d = list(self.index_values_array_1d )
            s[i].index_values_array_2d = list(self.index_values_array_2d )
            s[i].values_array_1d = list(self.values_array_1d )
            s[i].values_array_2d = list(self.values_array_2d )
        return s
