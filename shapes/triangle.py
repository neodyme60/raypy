from core.bbox import BoundingBox
from core.shape import Shape
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.intersection import Intersection
from core.transform import Transform


class TriangleMesh(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, p:[Point3d], v: [Vector3d], vi: [int], n: [Normal]):
        super().__init__(o2w, w2o)
        self.vertices = v
        self.normals = n
        self.points = p
        self.vertex_index = vi

    def get_object_bound(self) -> BoundingBox:
        bb = BoundingBox()
        for p in self.points:
            bb = bb.get_union_point3d(p)
        return bb

    def get_world_bound(self) -> BoundingBox:
        bb = BoundingBox()
        for p in self.points:
            bb = bb.get_union_point3d(p * self.objectToWorld)
        return bb

    def get_refine(self, shapes: [Shape]):
        for i in range(self.vertex_index/3):
            shapes.append(Triangle(self.objectToWorld, self. worldToObject, self, i))


class Triangle(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, mesh: TriangleMesh, index: int):
        super().__init__(o2w, w2o)
        self.mesh = mesh
        self.index0 = index

    def get_can_intersect(self)->bool:
        return True

    def get_object_bound(self) -> BoundingBox:
        p1_index = self.mesh.vertex_index[self.index0 + 0]
        p2_index = self.mesh.vertex_index[self.index0 + 1]
        p3_index = self.mesh.vertex_index[self.index0 + 2]

        p1 = self.mesh.points[p1_index * 3 + 0]
        p2 = self.mesh.points[p2_index * 3 + 1]
        p3 = self.mesh.points[p3_index * 3 + 2]
        bb = BoundingBox(p1, p2).get_union_point3d(p3)
        return bb

    def get_world_bound(self) -> BoundingBox:
        p1_index = self.mesh.vertex_index[self.index0 + 0]
        p2_index = self.mesh.vertex_index[self.index0 + 1]
        p3_index = self.mesh.vertex_index[self.index0 + 2]

        p1 = self.mesh.points[p1_index * 3 + 0]
        p2 = self.mesh.points[p2_index * 3 + 1]
        p3 = self.mesh.points[p3_index * 3 + 2]
        bb = BoundingBox(p1, p2).get_union_point3d(p3)
        return bb

    def get_intersection(self, ray, intersection: Intersection) -> bool:
        p1_index = self.mesh.vertex_index[self.index0 + 0]
        p2_index = self.mesh.vertex_index[self.index0 + 1]
        p3_index = self.mesh.vertex_index[self.index0 + 2]

        p1 = self.mesh.points[p1_index * 3 + 0]
        p2 = self.mesh.points[p2_index * 3 + 1]
        p3 = self.mesh.points[p3_index * 3 + 2]

        e1 = p2 - p1
        e2 = p3 - p1
        s1 = Vector3d.cross(ray.direction, e2)
        divisor = Vector3d.dot(s1, e1)

        if divisor == 0.0:
            return False
        invDivisor = 1.0 / divisor

        # Compute first barycentric coordinate
        d = ray.o - p1
        b1 = Vector3d.dot(d, s1) * invDivisor
        if b1 < 0.0 or b1 > 1.0:
            return False

        #Compute second barycentric coordinate
        s2 = Vector3d.cross(d, e1)
        b2 = Vector3d.dot(ray.d, s2) * invDivisor
        if b2 < 0.0 or b1 + b2 > 1.0:
            return False

        # Compute _t_ to intersection point
        t = Vector3d.dot(e2, s2) * invDivisor
        if t < ray.mint or t > ray.maxt:
            return False

        intersection.differentialGeometry.shape = self
        intersection.differentialGeometry.point = ray.get_at(t)
        intersection.ray_epsilon = t

        return True


    def get_is_intersected(self, ray) -> bool:
        p1_index = self.mesh.vertex_index[self.index0 + 0]
        p2_index = self.mesh.vertex_index[self.index0 + 1]
        p3_index = self.mesh.vertex_index[self.index0 + 2]

        p1 = self.mesh.points[p1_index * 3 + 0]
        p2 = self.mesh.points[p2_index * 3 + 1]
        p3 = self.mesh.points[p3_index * 3 + 2]

        e1 = p2 - p1
        e2 = p3 - p1
        s1 = Vector3d.cross(ray.direction, e2)
        divisor = Vector3d.dot(s1, e1)

        if divisor == 0.0:
            return False
        invDivisor = 1.0 / divisor

        # Compute first barycentric coordinate
        d = ray.o - p1
        b1 = Vector3d.dot(d, s1) * invDivisor
        if b1 < 0.0 or b1 > 1.0:
            return False

        #Compute second barycentric coordinate
        s2 = Vector3d.cross(d, e1)
        b2 = Vector3d.dot(ray.d, s2) * invDivisor
        if b2 < 0.0 or b1 + b2 > 1.0:
            return False

        # Compute _t_ to intersection point
        t = Vector3d.dot(e2, s2) * invDivisor
        if t < ray.mint or t > ray.maxt:
            return False

        return True
