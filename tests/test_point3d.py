from unittest import TestCase
from maths.point3d import Point3d
from core.transform import Transform


class TestPoint3d(TestCase):

    def test_mul_transform(self):

        #=========================================== point3d * transform
        foo1 = Point3d(0.0, 0.0, 0.0)
        foo2 = Transform.create_translate(1.0, 2.0, 3.0)
        foo3 = foo1 * foo2

        self.assertEqual(foo3, Point3d(1.0, 2.0, 3.0))
