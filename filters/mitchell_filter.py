from core.filter import Filter


class MitchellFilter(Filter):
    def __init__(self, width: float, height: float):
        super().__init__(width, height)

    def evaluate(self, x: float, y: float) -> float:
        return 1.0