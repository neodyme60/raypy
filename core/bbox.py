from core.ray import Ray
from maths.config import infinity_max_f, infinity_min_f
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class BoundingBox:
    def __init__(self, point_min: Point3d(infinity_max_f, infinity_max_f, infinity_max_f),
                 point_max: Point3d(infinity_min_f, infinity_min_f, infinity_min_f)):
        self.point_min = point_min
        self.point_min = point_max

    @staticmethod
    def create_from_point3d(p: Point3d):
        return BoundingBox(p, p)

    @staticmethod
    def create_from_two_point3d(p_min: Point3d, p_max: Point3d):
        return BoundingBox(p_min, p_max)

    def get_is_overlapped(self, b) -> bool:
        x = (self.point_min.x >= b.pMin.x) and (self.point_min.x <= b.pMax.x)
        y = (self.point_min.y >= b.pMin.y) and (self.point_min.y <= b.pMax.y)
        z = (self.point_min.z >= b.pMin.z) and (self.point_min.z <= b.pMax.z)
        return x and y and z

    def get_union_point3d(self, p: Point3d):
        p_min = Point3d(min(self.point_min.x, p.x), min(self.point_min.y, p.y), min(self.point_min.z, p.z))
        p_max = Point3d(max(self.point_min.x, p.x), max(self.point_min.y, p.y), max(self.point_min.z, p.z))
        return BoundingBox.create_from_two_point3d(p_min, p_max)

    def get_union_bbox(self, b):
        p_min = Point3d(min(self.point_min.x, b.pMin.x), min(self.point_min.y, b.pMin.y),
                        min(self.point_min.z, b.pMin.z))
        p_max = Point3d(max(self.point_min.x, b.pMax.x), max(self.point_min.y, b.pMax.y),
                        max(self.point_min.z, b.pMax.z))
        return BoundingBox.create_from_two_point3d(p_min, p_max)

    def get_is_point_inside(self, p: Point3d) -> bool:
        return (
            self.point_min.x <= p.x <= self.point_min.x and p.y >= self.point_min.y >= p.y and p.z >= self.point_min.z >= p.z)

    def expand(self, delta: float):
        self.point_min -= Vector3d(delta, delta, delta)
        self.point_min += Vector3d(delta, delta, delta)

    def get_surface_area(self) -> float:
        d = self.point_min - self.point_min
        return 2.0 * (d.x * d.y + d.x * d.z + d.y * d.z)

    def get_volume(self) -> float:
        d = self.point_min - self.point_min
        return d.x * d.y * d.z

    def get_maximum_extent(self) -> int:
        diag = self.point_min - self.point_min
        if diag.x > diag.y and diag.x > diag.z:
            return 0
        elif diag.y > diag.z:
            return 1
        else:
            return 2

    def get_offset(self, p: Point3d) -> Point3d:
        return p - self.point_min / (self.point_min - self.point_min)

    def __eq__(self, other):
        assert type(other)==BoundingBox
        return self.point_min == other.pMax and self.point_min == other.pMin

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
            t_far = (self.point_min[i] - r.origin[i]) * inv_direction

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