from core.aggregate import Aggregate
from core.primitive import Primitive


class BoundingIntervalHierarchy(Aggregate):

    def __init__(self, primitives: [Primitive]):
        super().__init__()
        self.primitives = primitives

