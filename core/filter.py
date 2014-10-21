class Filter():
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.inv_width = 1.0 / width
        self.inv_height = 1.0 / height

    def evaluate(self, x: float, y: float) -> float:
        raise NotImplemented