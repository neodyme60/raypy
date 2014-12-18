import math
from core.bbox import BoundingBox
from core.differential_geometry import DifferentialGeometry
from core.monte_carlo import UniformConePdf, UniformSampleSphere, UniformSampleCone2
from core.sample import Sample
from core.shape import Shape
import maths
from maths.normal import Normal
from maths.point3d import Point3d
from maths.tools import get_clamp
from maths.vector3d import Vector3d
from core.transform import Transform
from core.ray import Ray
from maths.vector4d import Vector4d


class Sphere(Shape):
    def __init__(self, o2w: Transform, w2o: Transform, radius: float, zmin: float, zmax: float, phimax: float):
        super().__init__(o2w, w2o)

        self.radius = radius
        self.zmin = get_clamp(min(zmin, zmax), -radius, radius)
        self.zmax = get_clamp(max(zmin, zmax), -radius, radius)
        self.thetaMin = math.acos(get_clamp(zmin/radius, -1.0, 1.0))
        self.thetaMax = math.acos(get_clamp(zmax/radius, -1.0, 1.0))
        self.phimax = math.radians(get_clamp(phimax, 0.0, 360.0))
        self.radius_squared = self.radius * self.radius

    def get_can_intersect(self):
        return True

    def internal_solve(self, ray_l: Ray, ray_w: Ray) -> (float, float):

        o = Vector3d.create_from_point3d(ray_l.origin)

        a = Vector3d.dot(ray_l.direction, ray_l.direction)
        b = 2.0 * Vector3d.dot(ray_l.direction, o)
        c = Vector3d.dot(o, o) - self.radius_squared

        # Solve quadratic equation for _t_ values
        t0, t1 = maths.tools.get_solve_quadratic(a, b, c)
        if t0 is None and t1 is None:
            return None, None

        # Compute intersection distance along ray
        if t0 > ray_w.max_t or t1 < ray_w.min_t:
            return None, None

        thit = t0
        if t0 < ray_w.min_t:
            thit = t1
        if thit > ray_w.max_t:
            return None, None
        return t0, t1

    def get_intersection(self, ray: Ray, dg: DifferentialGeometry) -> (bool, float):

        # ray from word_space_to_object_space
        ray_o = ray * self.worldToObject

        t0, t1 = self.internal_solve(ray_o, ray)

        if t0 is None and t1 is None:
            return False, 0.0

        if ray_o.min_t <= t0 < ray_o.max_t:
            dg.point = ray_o.get_at(t0) * self.objectToWorld
            # intersection.differentialGeometry.point = ray.get_at(intersection.ray_epsilon)
            # * self.objectToWorld
            # intersection.differentialGeometry.normal = Normal.create_from_point3d(intersection.differentialGeometry.point);

            v = Vector4d(dg.point.x, dg.point.y, dg.point.z, 1.0) * self.worldToObject
            v = Vector3d(v.x, v.y, v.z).get_normalized()
            dg.normal = Normal(v.x, v.y, v.z) * self.objectToWorld
            dg.shape = self
            return True, t0
        return False, 0.0

    def get_is_intersected(self, ray: Ray) -> bool:

        # ray from world_space_to_object_space
        ray_o = ray * self.worldToObject

        t0, t1 = self.internal_solve(ray_o, ray)

        return t0 is not None and t1 is not None

    def get_object_bound(self) -> BoundingBox:
        return BoundingBox(Point3d(-self.radius, -self.radius, -self.radius),
                           Point3d(self.radius, self.radius, self.radius))

    def Area(self):
        return self.phimax * self.radius * (self.zmax - self.zmin)

    def Pdf2(self, p: Point3d, wi: Vector3d) -> float:
        Pcenter = Point3d(0, 0, 0) * self.objectToWorld

        ds = (p - Pcenter).get_length_squared()

        # Return uniform weight if point inside sphere
        if ds - self.radius * self.radius < 1e-4:
            return super().Pdf2(p, wi)

        # Compute general sphere weight
        sinThetaMax2 = self.radius * self.radius / ds
        cosThetaMax = math.sqrt(max(0.0, 1.0 - sinThetaMax2))
        return UniformConePdf(cosThetaMax)

    def Sample2(self, p: Point3d, u: (float, float), Ns: Normal) -> Point3d:
        # Compute coordinate system for sphere sampling
        Pcenter = Point3d(0, 0, 0) * self.objectToWorld
        wc = (Pcenter - p).get_normalized()
        wcX, wcY = Transform.create_coordinateSystem(wc)

        # Sample uniformly on sphere if $\pt{}$ is inside it
        if (p - Pcenter).get_length_squared() - self.radius * self.radius < 1e-40:
            return self.Sample1(u, Ns)

        # Sample sphere uniformly inside subtended cone
        sinThetaMax2 = self.radius * self.radius / (p - Pcenter).get_length_squared()
        cosThetaMax = math.sqrt(max(0.0, 1.0 - sinThetaMax2))
        dgSphere = DifferentialGeometry()

        thit = 1.0

        r = Ray(p, UniformSampleCone2(u, cosThetaMax, wcX, wcY, wc), 1e-3)
        b, t = self.get_intersection(r, dgSphere)
#        if not b:
        #bug
        thit = Vector3d.dot(Pcenter - p, r.direction.get_normalized())
        ps = r.get_at(thit)

        nn = (ps - Pcenter).get_normalized()
        Ns.Set(nn)
        # if (ReverseOrientation) *ns *= -1.f;
        return ps

    def Sample1(self, u: (float, float), Ns: Normal) -> Point3d:
        p = Point3d(0, 0, 0) + UniformSampleSphere(u) * self.radius
        Ns.Set((Normal(p.x, p.y, p.z) * self.objectToWorld).get_normalized())
        # if (ReverseOrientation) *ns *= -1.f;
        return p * self.objectToWorld


