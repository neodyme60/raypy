from unittest import TestCase

from maths.vector3d import Vector3d


__author__ = 'nicolas'


class TestVector3d(TestCase):
    def test_dot(self):
        foo1 = Vector3d(1.0, 2.0, 3.0)
        foo2 = Vector3d(10.0, 20.0, 30.0)
        foo3 = Vector3d.dot(foo1,foo2)
        self.assertEqual(foo3, foo1.x * foo2.x + foo1.y * foo2.y + foo1.z * foo2.z)

    def test_setZero(self):
        foo = Vector3d(1.0, 2.0, 3.0)
        foo.set_to_zero()
        self.assertEqual(foo.x, 0.0)
        self.assertEqual(foo.y, 0.0)
        self.assertEqual(foo.z, 0.0)