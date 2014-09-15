__author__ = 'nicolas'

class Film:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [int]* (width*height)


    def generate_ray(self):
        raise Exception("Must be implemented")