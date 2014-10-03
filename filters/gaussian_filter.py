import math

from core.filter import Filter


class GaussianFilter(Filter):
    def __init__(self, width: float, height: float, alpha: float):
        Filter.__init__(self, width, height)
        self.alpha = alpha
        self.exp_x = math.exp(-self.alpha * self.width * self.width)
        self.exp_y = math.exp(-self.alpha * self.height * self.height)

    def evaluate(self, x: float, y: float) -> float:
        return self.get_gaussian(x, self.exp_x) * self.get_gaussian(y, self.exp_y)

    def get_gaussian(self, d: float, exp_v: float) -> float:
        return max(0.0, float(math.exp(-self.alpha * d * d) - exp_v))