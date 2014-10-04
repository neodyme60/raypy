from core.transform import Transform


class Light:

    def __init__(self, l2w: Transform, samples_count: int=1):
        self.lightToWorld = l2w
        self.worldToObject = l2w.get_invert()
        self.samples_count = max(1, samples_count)
