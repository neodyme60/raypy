import math

from core.filter import Filter


class LanczosSincFilter(Filter):
    def __init__(self, width: float, height: float, tau: float):
        Filter.__init__(self, width, height)
        self.tau = tau

    def evaluate(self, x: float, y: float) -> float:
        return self.sinc_1d(x * self.inv_width) * self.sinc_1d(y * self.inv_width)

    def sinc_1d(self, x: float) -> filter:
        x = math.fabs(x)
        if x < 1e-5:
            return 1.0
        if x > 1.0:
            return 0.0
        x *= math.pi
        sinc = math.sin(x) / x
        lanczos = math.sin(x * self.tau) / (x * self.tau)
        return sinc * lanczos