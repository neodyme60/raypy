from PIL import Image
from aggregates.simple import Simple


class Scene():

    def __init__(self, ):
        self.aggregate = Simple()

    def add_geometry(self, other):
        self.aggregate.add(other)
