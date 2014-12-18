import math

from core.filter import Filter


class TriangleFilter(Filter):
    def __init__(self, width: float, height: float, b: float, c: float):
        super().__init__(width, height)
        self.b = b
        self.c = c

    def evaluate(self, x: float, y: float) -> float:
        return self.mitchell_1d(x * self.inv_width) * self.mitchell_1d(y * self.inv_height)

    def mitchell_1d(self, x: float) -> float:
        x = math.fabs(2.0 * x)
        if x > 1.0:
            return ((-self.b - 6.0 * self.C) * x * x * x + (6.0 * self.b + 30.0 * self.c) * x * x + (
                -12.0 * self.b - 48.0 * self.c) * x + (8.0 * self.b + 24.0 * self.c)) * (1.0 / 6.0)
        else:
            return ((12.0 - 9.0 * self.b - 6.0 * self.c) * x * x * x +
                    (-18.0 + 12.0 * self.b + 6.0 * self.c) * x * x +
                    (6.0 - 2.0 * self.b)) * (1.0 / 6.0)
