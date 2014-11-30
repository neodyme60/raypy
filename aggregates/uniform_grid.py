import math

from core.aggregate import Aggregate
from core.bbox import BoundingBox
from core.intersection import Intersection
from core.primitive import Primitive
from core.ray import Ray
import maths
from maths.normal import Normal
from maths.point3d import Point3d
from maths.tools import get_clamp
from maths.vector3d import Vector3d


class Voxel:
    def __init__(self, primitive):
        self.primitives = [primitive]
        self.allCanIntersect = False

    def get_size(self) -> int:
        return len(self.primitives)

    def add_primitive(self, primitive: Primitive):
        self.primitives.append(primitive)

    def get_is_intersected(self, ray: Ray) -> bool:
        # Refine primitives in voxel if needed
        if not self.allCanIntersect:
            for i in range(len(self.primitives)):
                prim = self.primitives[i]
                # Refine primitive _prim_ if it's not intersectable
                if not prim.get_can_intersect():
                    prims = []
                    prim.get_fully_refine(prims)
                    assert len(prims) > 0
                    if len(prims) == 1:
                        self.primitives[i] = prims[0]
                    else:
                        self.primitives[i] = UniformGrid(prims, False)
        self.allCanIntersect = True

        # Loop over primitives in voxel and find intersections
        for prim in self.primitives:
            if prim.get_is_intersected(ray):
                return True

        return False

    def get_intersection(self, ray: Ray, intersection: Intersection) -> bool:
        # Refine primitives in voxel if needed
        if not self.allCanIntersect:
            for i in range(len(self.primitives)):
                prim = self.primitives[i]
                # Refine primitive _prim_ if it's not intersectable
                if not prim.get_can_intersect():
                    prims = []
                    prim.get_fully_refine(prims)
                    assert len(prims) > 0
                    if len(prims) == 1:
                        self.primitives[i] = prims[0]
                    else:
                        self.primitives[i] = UniformGrid(prims, False)
        self.allCanIntersect = True

        # Loop over primitives in voxel and find intersections
        hitSomething = False
        intersection_tmp = Intersection()
        for prim in self.primitives:
            if prim.get_intersection(ray, intersection_tmp):
                if intersection_tmp.ray_epsilon < intersection.ray_epsilon:
                    intersection.ray_epsilon = intersection_tmp.ray_epsilon
                    intersection.differentialGeometry.point = intersection_tmp.differentialGeometry.point
                    intersection.differentialGeometry.normal = intersection_tmp.differentialGeometry.normal
                    intersection.differentialGeometry.shape = intersection_tmp.differentialGeometry.shape
                    hitSomething = True
        return hitSomething


class UniformGrid(Aggregate):
    def __init__(self, primitives: [Primitive], refine_immediately: bool):
        super().__init__()
        self.voxels = []
        self.bounds = BoundingBox()
        self.width = Vector3d()
        self.inv_width = Vector3d()
        self.nVoxels = [int] * 3
        self.primitives = []

        # Initialize _primitives_ with primitives for grid
        if refine_immediately:
            for p in primitives:
                p.get_fully_refine(self.primitives)
        else:
            self.primitives = primitives

        # Compute bounds and choose grid resolution
        for p in self.primitives:
            self.bounds = BoundingBox.get_union_bbox(self.bounds, p.get_world_bound())
        delta = self.bounds.point_max - self.bounds.point_min

        #Find _voxelsPerUnitDist_ for grid
        maxAxis = self.bounds.get_maximum_extent()
        invMaxWidth = 1.0 / delta[maxAxis]
        assert (invMaxWidth > 0.0)
        cubeRoot = 3.0 * pow(float(len(self.primitives)), 1.0 / 3.0)
        voxelsPerUnitDist = cubeRoot * invMaxWidth
        for axis in range(3):
            self.nVoxels[axis] = int(math.floor(delta[axis] * voxelsPerUnitDist))
            self.nVoxels[axis] = maths.tools.get_clamp(self.nVoxels[axis], 1, 64)

        # Compute voxel widths and allocate voxels
        for axis in range(3):
            self.width[axis] = delta[axis] / self.nVoxels[axis]
            if self.width[axis] == 0.0:
                self.inv_width[axis] = 0.0
            else:
                self.inv_width[axis] = 1.0 / self.width[axis]

        nv = self.nVoxels[0] * self.nVoxels[1] * self.nVoxels[2]
        self.voxels = [None] * nv

        #Add primitives to grid voxels
        for p in self.primitives:
            # Find voxel extent of primitive
            pb = p.get_world_bound()
            vmin = [int] * 3
            vmax = [int] * 3
            for axis in range(3):
                vmin[axis] = self.get_pos_to_voxel(pb.point_min, axis)
                vmax[axis] = self.get_pos_to_voxel(pb.point_max, axis)

            # Add primitive to overlapping voxels
            for z in range(vmin[2], vmax[2]+1):
                for y in range(vmin[1], vmax[1]+1):
                    for x in range(vmin[0], vmax[0]+1):
                        o = self.get_offset(x, y, z)
                        if self.voxels[o] is None:
                            # Allocate new voxel and store primitive in it
                            self.voxels[o] = Voxel(p)
                        else:
                            # Add primitive to already-allocated voxel
                            self.voxels[o].add_primitive(p)

    def get_world_bound(self):
        return self.bounds

    def get_can_intersect(self):
        return True

    def get_is_intersected(self, ray: Ray) -> bool:

        # Check ray against overall grid bounds
        if self.bounds.get_is_point_inside(ray.get_at(ray.min_t)):
            rayT = ray.min_t
        else:
            rayT, tmp = self.bounds.get_intersect(ray)
            if rayT == None:
                return False

        gridIntersect = ray.get_at(rayT)


#        return True


        # Set up 3D DDA for ray
        NextCrossingT = [float] * 3
        DeltaT = [float] * 3
        Step = [int] * 3
        Out = [int] * 3
        Pos = [int] * 3
        for axis in range(3):
            # Compute current voxel for axis
            Pos[axis] = self.get_pos_to_voxel(gridIntersect, axis)
            if ray.direction[axis] >= 0:
                # Handle ray with positive direction for voxel stepping
                NextCrossingT[axis] = rayT + (self.get_voxel_to_pos(Pos[axis] + 1, axis) - gridIntersect[axis]) / \
                                             ray.direction[axis]
                DeltaT[axis] = self.width[axis] / ray.direction[axis]
                Step[axis] = 1
                Out[axis] = self.nVoxels[axis]
            else:
                # Handle ray with negative direction for voxel stepping
                NextCrossingT[axis] = rayT + (self.get_voxel_to_pos(Pos[axis], axis) - gridIntersect[axis]) / \
                                             ray.direction[axis]
                DeltaT[axis] = -self.width[axis] / ray.direction[axis]
                Step[axis] = -1
                Out[axis] = -1

        #Walk grid for shadow ray
        while True:
            o = self.get_offset(Pos[0], Pos[1], Pos[2])
            voxel = self.voxels[o]
            if voxel != None:
                if voxel.get_is_intersected(ray):
                    return True
            # Advance to next voxel

            # Find _stepAxis_ for stepping to next voxel
            bits = ((NextCrossingT[0] < NextCrossingT[1]) << 2) + ((NextCrossingT[0] < NextCrossingT[2]) << 1) + (
            (NextCrossingT[1] < NextCrossingT[2]))
            cmpToAxis = [2, 1, 2, 1, 2, 2, 0, 0]
            stepAxis = cmpToAxis[bits]
            if ray.max_t < NextCrossingT[stepAxis]:
                break
            Pos[stepAxis] += Step[stepAxis]
            if Pos[stepAxis] == Out[stepAxis]:
                break
            NextCrossingT[stepAxis] += DeltaT[stepAxis]
        return False

    def get_intersection(self, ray: Ray, intersection: Intersection) -> bool:
        # Check ray against overall grid bounds
        if self.bounds.get_is_point_inside(ray.get_at(ray.min_t)):
            rayT = ray.min_t
        else:
            rayT, tmp = self.bounds.get_intersect(ray)
            if rayT == None:
                return False
        gridIntersect = ray.get_at(rayT)


#        intersection.differentialGeometry.point = gridIntersect
#        intersection.differentialGeometry.shape = self
#        intersection.differentialGeometry.normal = Normal(gridIntersect.x, gridIntersect.y, gridIntersect.z)
#        return True

        # Set up 3D DDA for ray
        NextCrossingT = [float] * 3
        DeltaT = [float] * 3
        Step = [int] * 3
        Out = [int] * 3
        Pos = [int] * 3
        for axis in range(3):
            # Compute current voxel for axis
            Pos[axis] = self.get_pos_to_voxel(gridIntersect, axis)
            if ray.direction[axis] >= 0:
                # Handle ray with positive direction for voxel stepping
                NextCrossingT[axis] = rayT + (self.get_voxel_to_pos(Pos[axis] + 1, axis) - gridIntersect[axis]) / \
                                             ray.direction[axis]
                DeltaT[axis] = self.width[axis] / ray.direction[axis]
                Step[axis] = 1
                Out[axis] = self.nVoxels[axis]
            else:
                # Handle ray with negative direction for voxel stepping
                NextCrossingT[axis] = rayT + (self.get_voxel_to_pos(Pos[axis], axis) - gridIntersect[axis]) / \
                                             ray.direction[axis]
                DeltaT[axis] = -self.width[axis] / ray.direction[axis]
                Step[axis] = -1
                Out[axis] = -1

        # Walk ray through voxel grid
        hitSomething = False
        while True:
            # Check for intersection in current voxel and advance to next
            voxel = self.voxels[self.get_offset(Pos[0], Pos[1], Pos[2])]
            if voxel != None:
                hitSomething |= voxel.get_intersection(ray, intersection)

            # Advance to next voxel

            # Find _stepAxis_ for stepping to next voxel
            bits = ((NextCrossingT[0] < NextCrossingT[1]) << 2) + ((NextCrossingT[0] < NextCrossingT[2]) << 1) + (
            (NextCrossingT[1] < NextCrossingT[2]))
            cmpToAxis = [2, 1, 2, 1, 2, 2, 0, 0]
            stepAxis = cmpToAxis[bits]
            if ray.max_t < NextCrossingT[stepAxis]:
                break
            Pos[stepAxis] += Step[stepAxis]
            if Pos[stepAxis] == Out[stepAxis]:
                break
            NextCrossingT[stepAxis] += DeltaT[stepAxis]
        return hitSomething

    def get_pos_to_voxel(self, point: Point3d, axis: int) -> int:
        v = int((point[axis] - self.bounds.point_min[axis]) * self.inv_width[axis])
        return get_clamp(v, 0, self.nVoxels[axis] - 1)

    def get_voxel_to_pos(self, p: int, axis: int) -> float:
        return self.bounds.point_min[axis] + p * self.width[axis]

    def get_offset(self, x: int, y: int, z: int) -> int:
        return z * self.nVoxels[0] * self.nVoxels[1] + y * self.nVoxels[0] + x
