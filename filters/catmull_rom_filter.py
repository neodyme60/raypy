import math

from core.filter import Filter


class CatmullRomFilter(Filter):
    def __init__(self, width: float, height: float):
        Filter.__init__(self, width, height)

    def evaluate(self, x: float, y: float) -> float:
        return self.catrom_1d(x) * self.catrom_1d(y)

    def catrom_1d(self, x: float) -> float:
        x = math.fabs(x)
        x2 = x * x
        x3 = x * x2
        if x >= 2:
            return 0
        if x < 1:
            return 3 * x3 - 5 * x2 + 2
        return -x3 + 5 * x2 - 8 * x + 4