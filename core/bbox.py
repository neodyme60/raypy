from core.ray import Ray
from core.transform import Transform
from maths.config import infinity_max_f, infinity_min_f
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class BoundingBox:
    def __init__(self, p_min : Point3d=Point3d(infinity_max_f, infinity_max_f, infinity_max_f), p_max : Point3d=Point3d(-infinity_max_f, -infinity_max_f, -infinity_max_f) ):
        self.point_min = p_min
        self.point_max = p_max

    @staticmethod
    def create_from_point3d(p: Point3d):
        return BoundingBox.create_from_two_point3d(p, p)

    @staticmethod
    def create_from_two_point3d(p1: Point3d, p2: Point3d):
        p_min = Point3d(min(p1.x, p2.x), min(p1.y, p2.y), min(p1.z, p2.z))
        p_max = Point3d(max(p1.x, p2.x), max(p1.y, p2.y), max(p1.z, p2.z))
        return BoundingBox(p_min, p_max)

    def get_is_overlapped(self, b) -> bool:
        x = (self.point_max.x >= b.point_min.x) and (self.point_min.x <= b.point_max.x)
        y = (self.point_max.y >= b.point_min.y) and (self.point_min.y <= b.point_max.y)
        z = (self.point_max.z >= b.point_min.z) and (self.point_min.z <= b.point_max.z)
        return x and y and z

    def get_union_point3d(self, p: Point3d):
        p_min = Point3d(min(self.point_min.x, p.x), min(self.point_min.y, p.y), min(self.point_min.z, p.z))
        p_max = Point3d(max(self.point_max.x, p.x), max(self.point_max.y, p.y), max(self.point_max.z, p.z))
        return BoundingBox(p_min, p_max)

    def get_union_bbox(self, b):
        p_min = Point3d(min(self.point_min.x, b.point_min.x), min(self.point_min.y, b.point_min.y),
                        min(self.point_min.z, b.point_min.z))
        p_max = Point3d(max(self.point_max.x, b.point_max.x), max(self.point_max.y, b.point_max.y),
                        max(self.point_max.z, b.point_max.z))
        return BoundingBox(p_min, p_max)

    def get_is_point_inside(self, p: Point3d) -> bool:
        return (
            self.point_min.x <= p.x <= self.point_max.x and
            self.point_min.y <= p.y <= self.point_max.y and
            self.point_min.z <= p.z <= self.point_max.z)

    def expand(self, delta: float):
        self.point_min -= Vector3d(delta, delta, delta)
        self.point_max += Vector3d(delta, delta, delta)

    def get_surface_area(self) -> float:
        d = self.point_min - self.point_min
        return 2.0 * (d.x * d.y + d.x * d.z + d.y * d.z)

    def get_volume(self) -> float:
        d = self.point_max - self.point_min
        return d.x * d.y * d.z

    def get_maximum_extent(self) -> int:
        diagonal = self.point_max - self.point_min
        if diagonal.x > diagonal.y and diagonal.x > diagonal.z:
            return 0
        elif diagonal.y > diagonal.z:
            return 1
        else:
            return 2

    def get_offset(self, p: Point3d) -> Point3d:
        return p - self.point_min / (self.point_max - self.point_min)

    def __eq__(self, other):
        assert type(other)==BoundingBox
        return self.point_max == other.pMax and self.point_min == other.pMin

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        raise NotImplemented

    def __gt__(self, other):
        raise NotImplemented

    def __ge__(self, other):
        raise NotImplemented

    def get_intersect(self, r: Ray) -> (float, float):
        t0 = r.min_t
        t1 = r.max_t
        for i in range(3):
            # Update interval for _i_th bounding box slab
            inv_direction = 1.0 / r.direction[i]
            t_near = (self.point_min[i] - r.origin[i]) * inv_direction
            t_far = (self.point_max[i] - r.origin[i]) * inv_direction

            # Update parametric interval from slab intersection $t$s
            if t_near > t_far:
                t_near, t_far = t_far, t_near
            if t_near > t0:
                t0 = t_near
            if t_far < t1:
                t1 = t_far
            if t0 > t1:
                return None, None
        return t0, t1