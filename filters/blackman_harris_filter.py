import math

from core.filter import Filter


class BlackmanHarrisFilter(Filter):
    def __init__(self, width: float, height: float):
        super().__init__(width, height)

    def evaluate(self, x: float, y: float) -> float:
        return self.bh_1d(x * self.inv_width * 2.0) * self.bh_1d(y * self.inv_heightinv * 2.0)

    def bh_1d(self, x: float) -> float:
        if x < -1.0 or x > 1.0:
            return 0.0
        x = (x + 1) * 0.5
        A0 = 0.35875
        A1 = -0.48829
        A2 = 0.14128
        A3 = -0.01168
        return float(
            A0 + A1 * math.cos(2 * math.pi * x) + A2 * math.cos(4 * math.pi * x) + A3 * math.cos(6 * math.pi * x))
