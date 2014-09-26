import numpy


class Film:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = numpy.random.random(width * height )*255
        self.data=numpy.reshape(self.data,(width, height))
        self.data=numpy.require(self.data, dtype = numpy.uint)

    def generate_ray(self):
        raise Exception("Must be implemented")