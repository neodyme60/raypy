from maths.point3d import Point3d
from maths.vector3d import Vector3d


class Intersection:
    def __init__(self):
        self.geometry = None
        self.distance = 0.0
        self.intersection = Point3d(0.0, 0.0, 0.0)
        self.normal = Vector3d().get_up()
