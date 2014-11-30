from core.bbox import BoundingBox
from core.differential_geometry import DifferentialGeometry
from core.ray import Ray
from core.shape import Shape
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.intersection import Intersection
from core.transform import Transform


class TriangleMesh(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, p:[Point3d], vi: [int], v: [Vector3d], n: [Normal]):
        super().__init__(o2w, w2o)
        self.vertices = v
        self.normals = n
        self.points = p
        self.index = vi

    def get_can_intersect(self)->bool:
        return False

    def get_object_bound(self) -> BoundingBox:
        bb = BoundingBox()
        for p in self.points:
            bb = bb.get_union_point3d(p)
        return bb

    def get_refine(self, shapes: [Shape]):
        for i in range(len(self.index)//3):
            shapes.append(Triangle(self.objectToWorld, self. worldToObject, self, i))


class Triangle(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, mesh: TriangleMesh, index: int):
        super().__init__(o2w, w2o)
        self.mesh = mesh
        self.triangle_index = index

    def get_can_intersect(self)->bool:
        return True

    def get_object_bound(self) -> BoundingBox:
        p1_index = self.mesh.index[self.triangle_index*3 + 0]
        p2_index = self.mesh.index[self.triangle_index*3 + 2]
        p3_index = self.mesh.index[self.triangle_index*3 + 1]

        p1 = self.mesh.points[p1_index]
        p2 = self.mesh.points[p2_index]
        p3 = self.mesh.points[p3_index]
        bb = BoundingBox(p1, p2).get_union_point3d(p3)
        return bb

    def get_intersection(self, ray: Ray, dg: DifferentialGeometry) -> (bool, float):
        p1_index = self.mesh.index[self.triangle_index*3 + 0]
        p2_index = self.mesh.index[self.triangle_index*3 + 2]
        p3_index = self.mesh.index[self.triangle_index*3 + 1]

        p1 = self.mesh.points[p1_index]
        p2 = self.mesh.points[p2_index]
        p3 = self.mesh.points[p3_index]

        e1 = p2 - p1
        e2 = p3 - p1
        s1 = Vector3d.cross(ray.direction, e2)
        divisor = Vector3d.dot(s1, e1)

        if divisor == 0.0:
            return (False, 0.0)
        invDivisor = 1.0 / divisor

        # Compute first barycentric coordinate
        d = ray.origin - p1
        b1 = Vector3d.dot(d, s1) * invDivisor
        if b1 < 0.0 or b1 > 1.0:
            return (False, 0.0)

        #Compute second barycentric coordinate
        s2 = Vector3d.cross(d, e1)
        b2 = Vector3d.dot(ray.direction, s2) * invDivisor
        if b2 < 0.0 or (b1 + b2) > 1.0:
            return (False, 0.0)

        # Compute _t_ to intersection point
        t = Vector3d.dot(e2, s2) * invDivisor
        if t < ray.min_t or t > ray.max_t:
            return (False, 0.0)

        dg.shape = self
        dg.point = ray.get_at(t)
        dg.normal = Normal.create_from_vector3d( Vector3d.cross(e1, e2).get_normalized())

        return (True, t)


    def get_is_intersected(self, ray) -> bool:
        p1_index = self.mesh.index[self.triangle_index*3 + 0]
        p2_index = self.mesh.index[self.triangle_index*3 + 2]
        p3_index = self.mesh.index[self.triangle_index*3 + 1]

        p1 = self.mesh.points[p1_index]
        p2 = self.mesh.points[p2_index]
        p3 = self.mesh.points[p3_index]

        e1 = p2 - p1
        e2 = p3 - p1
        s1 = Vector3d.cross(ray.direction, e2)
        divisor = Vector3d.dot(s1, e1)

        if divisor == 0.0:
            return False
        invDivisor = 1.0 / divisor

        # Compute first barycentric coordinate
        d = ray.origin - p1
        b1 = Vector3d.dot(d, s1) * invDivisor
        if b1 < 0.0 or b1 > 1.0:
            return False

        #Compute second barycentric coordinate
        s2 = Vector3d.cross(d, e1)
        b2 = Vector3d.dot(ray.direction, s2) * invDivisor
        if b2 < 0.0 or (b1 + b2) > 1.0:
            return False

        # Compute _t_ to intersection point
        t = Vector3d.dot(e2, s2) * invDivisor
        if t < ray.min_t or t > ray.max_t:
            return False

        return True
