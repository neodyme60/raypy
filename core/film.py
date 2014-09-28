import numpy


class Film:

    def __init__(self, width, height):
        self.width = width
        self.height = height
#        self.data = numpy.random.random(width * height )*255
        self.data = numpy.random.random(width * height )*0
        self.data=numpy.reshape(self.data,(height, width))
        self.data=numpy.require(self.data, dtype = numpy.uint)

    def generate_ray(self):
        raise Exception("Must be implemented")