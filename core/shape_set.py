from core.differential_geometry import DifferentialGeometry
from core.distribution1d import Distribution1D
from core.light_sample import LightSample
from core.ray import Ray
from core.shape import Shape
from maths.config import infinity_max_f
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class ShapeSet:

    def __init__(self, shape: Shape):
        self.shapes = []
        self.sumArea = 0.0
        self.areas = []
        self.areaDistribution = []

        todo = [shape]
        while len(todo)>0:
            sh = todo.pop()
            if sh.get_can_intersect():
                self.shapes.append(sh)
            else:
                sh.get_refine(todo)

        self.sumArea = 0.0
        for i in range(len(self.shapes)):
            area = self.shapes[i].Area()
            self.areas.append(area)
            self.sumArea += area

        self.areaDistribution = Distribution1D(self.areas)

    def Sample1(self, p: Point3d, ls: LightSample, Ns: Normal)->Point3d:
        pdf, sn = self.areaDistribution.SampleDiscrete(ls.uComponent)
        pt = self.shapes[sn].Sample2(p, ls.uPos, Ns)

        # Find closest intersection of ray with shapes in _ShapeSet_
        r = Ray(p, (pt-p).get_normalized(), 1e-3, infinity_max_f)
        anyHit = False
        thit = 1.0
        dg = DifferentialGeometry()
        for i in range(len(self.shapes)):
            anyHit_b, thit_f = self.shapes[i].get_intersection(r, dg)
            if anyHit_b:
                anyHit = True
                thit = thit_f
        if anyHit:
            Ns.Set(dg.normal)
        return r.get_at(thit)

    def Sample2(self, ls: LightSample,  n: Normal)->Point3d:
        pdf, sn = self.areaDistribution.SampleDiscrete(ls.uComponent)
        return self.shapes[sn].Sample1(ls.uPos, n)

    def Area(self):
        return self.sumArea

    def Pdf1(self, p: Point3d)->float:
        pdf = 0.0
        for i in range(len(self.shapes)):
            pdf += self.areas[i] * self.shapes[i].Pdf1(p)
        return pdf / self.sumArea

    def Pdf2(self, p: Point3d, wi: Vector3d)->float:
        pdf = 0.0
        for i in range(len(self.shapes)):
            pdf += self.areas[i] * self.shapes[i].Pdf2(p, wi)
        return pdf / self.sumArea

