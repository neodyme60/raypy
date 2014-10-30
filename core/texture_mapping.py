import math

from core.differential_geometry import DifferentialGeometry
from core.transform import Transform
from maths.config import CONST_TWOPI_INV, CONST_PI_INV
from maths.point3d import Point3d
from maths.tools import get_spherical_theta, get_spherical_phi
from maths.vector3d import Vector3d


class TextureMapping2D:
    def __init__(self):
        pass

    def get_map(self, differential_geometry: DifferentialGeometry):
        raise  NotImplemented

class UVMapping2D(TextureMapping2D):
    def __init__(self):
        super().__init__()

class SphericalMapping2D(TextureMapping2D):
    def __init__(self, worldToSphere: Transform):
        TextureMapping2D.__init__(self)
        self.WorldToTexture = worldToSphere

    def _internal_sphere(self, p: Point3d):
        vec = (p*self.WorldToTexture - Point3d(0,0,0)).get_normalized()
        theta = get_spherical_theta(vec)
        phi = get_spherical_phi(vec)
        s = theta * CONST_PI_INV
        t = phi * CONST_TWOPI_INV
        return s, t

    def get_map(self, dg: DifferentialGeometry):
        s,t = self._internal_sphere(dg.point)
        delta = 0.1

        sx, tx = self._internal_sphere(dg.point + delta * dg.dpdx)
        dsdx = (sx - s) / delta
        dtdx = (tx - t) / delta
        if dtdx > 0.5:
            dtdx = 1.0 - dtdx
        elif dtdx < - 0.5:
            dtdx = -(dtdx + 1)

        sy, ty = self._internal_sphere(dg.point + delta * dg.dpdy)
        dsdy = (sy - s) / delta
        dtdy = (ty - t) / delta
        if dtdy > .5:
            dtdy = 1.0 - dtdy
        elif dtdy < -0.5:
            dtdy = -(dtdy + 1)
        return s,t ,dsdx, dtdx, dsdy, dtdy

class CylindricalMapping2D(TextureMapping2D):
    def __init__(self, worldToCyl: Transform):
        super().__init__()
        self.WorldToTexture = worldToCyl

    def _internal_cylinder(self, p: Point3d):
        vec = (p*self.WorldToTexture - Point3d(0,0,0)).get_normalized()
        s = (math.pi + math.atan2(vec.y, vec.x)) / (2.0 * math.pi)
        t = vec.z
        return s, t

    def get_map(self, dg: DifferentialGeometry):
        s,t = self._internal_cylinder(dg.point)
        delta = 0.01

        sx, tx = self._internal_cylinder(dg.point + delta * dg.dpdx)
        dsdx = (sx - s) / delta
        dtdx = (tx - t) / delta
        if dtdx > 0.5:
            dtdx = 1.0 - dtdx
        elif dtdx < - 0.5:
            dtdx = -(dtdx + 1)

        sy, ty = self._internal_cylinder(dg.point + delta * dg.dpdy)
        dsdy = (sy - s) / delta
        dtdy = (ty - t) / delta
        if dtdy > 0.5:
            dtdy = 1.0 - dtdy
        elif dtdy < - 0.5:
            dtdy = -(dtdy + 1)

        return s,t ,dsdx, dtdx, dsdy, dtdy

class PlanarMapping2D(TextureMapping2D):
    def __init__(self, vv1: Vector3d, vv2: Vector3d, dds: float=0.0, ddt: float=0.0):
        super().__init__()
        self.vs = vv1
        self.vt = vv2
        self.ds = dds
        self.dt = ddt

    def get_map(self, dg: DifferentialGeometry):
        vec = dg.point - Point3d(0,0,0)
        s = self.ds + Vector3d.dot(vec, self.vs)
        t = self.dt + Vector3d.dot(vec, self.vt)
        dsdx = Vector3d.dot(dg.dpdx, self.vs)
        dtdx = Vector3d.dot(dg.dpdx, self.vt)
        dsdy = Vector3d.dot(dg.dpdy, self.vs)
        dtdy = Vector3d.dot(dg.dpdy, self.vt)

        return s,t ,dsdx, dtdx, dsdy, dtdy

class TextureMapping3D:
    def __init__(self):
        pass

class IdentityMapping3D(TextureMapping2D):
    def __init__(self):
        super().__init__()

