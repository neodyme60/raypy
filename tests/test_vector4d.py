from unittest import TestCase
import math

from maths.vector4d import Vector4d
from core.transform import Transform


__author__ = 'nicolas'


class TestVector4d(TestCase):
    def test_dot(self):
        foo1 = Vector4d(1.0, 2.0, 3.0, 4.0)
        foo2 = Vector4d(10.0, 20.0, 30.0, 40.0)
        foo3 = foo1.dot(foo2)
        self.assertEqual(foo3, foo1.x * foo2.x + foo1.y * foo2.y + foo1.z * foo2.z + foo1.w * foo2.w)

    def test_set_to_zero(self):
        # ///////////////////////////////////////////set_to_zero
        foo = Vector4d(1.0, 2.0, 3.0, 4.0)
        foo.set_to_zero()
        self.assertEqual(foo.x, 0.0)
        self.assertEqual(foo.y, 0.0)
        self.assertEqual(foo.y, 0.0)
        self.assertEqual(foo.z, 0.0)

        self.assertEqual(foo, Vector4d(0.0, 0.0, 0.0, 0.0))

    def test___mul__(self):
        # ///////////////////////////////////////////__mul__ float
        foo1 = Vector4d(1.0, 2.0, 3.0, 4.0)
        foo2 = foo1 * 2.0

        self.assertEqual(foo2, Vector4d(2.0, 4.0, 6.0, 8.0))

        #///////////////////////////////////////////__imul__ float
        foo1 = Vector4d(1.0, 2.0, 3.0, 4.0)
        foo1 *= 2.0
        self.assertEqual(foo1, Vector4d(2.0, 4.0, 6.0, 8.0))

        #///////////////////////////////////////////__mul__ vector4d
        foo1 = Vector4d(1.0, 2.0, 3.0, 4.0)
        foo2 = Vector4d(2.0, 3.0, 4.0, 5.0)
        foo3 = foo1 * foo2
        self.assertEqual(foo3, Vector4d(2.0, 6.0, 12.0, 20.0))

        #///////////////////////////////////////////__imul__ vector4d
        foo1 = Vector4d(1.0, 2.0, 3.0, 4.0)
        foo1 *= Vector4d(2.0, 3.0, 4.0, 5.0)
        self.assertEqual(foo1, Vector4d(2.0, 6.0, 12.0, 20.0))

        #///////////////////////////////////////////__mul__ matrix44 Rotz
        foo1 = Vector4d(0.0, 2.0, 0.0, 1.0)
        foo2 = Transform.create_rot_z(math.radians(90))

        foo3 = foo1 * foo2.mat
        self.assertEqual(foo3, Vector4d(-2.0, 0.0, 0.0, 1.0))

        foo3 = foo3 * foo2.mat
        self.assertEqual(foo3, Vector4d(0.0, -2.0, 0.0, 1.0))

        #///////////////////////////////////////////__mul__ matrix44 Roty
        foo1 = Vector4d(2.0, 0.0, 0.0, 1.0)
        foo2 = Transform.create_rot_y(math.radians(90))

        foo3 = foo1 * foo2.mat
        self.assertEqual(foo3, Vector4d(0.0, 0.0, -2.0, 1.0))

        foo3 = foo3 * foo2.mat
        self.assertEqual(foo3, Vector4d(-2.0, 0.0, 0.0, 1.0))

        #///////////////////////////////////////////__mul__ matrix44 Rotx
        foo1 = Vector4d(0.0, 2.0, 0.0, 1.0)
        foo2 = Transform.create_rot_x(math.radians(90))

        foo3 =  foo1 * foo2.mat
        self.assertEqual(foo3, Vector4d(0.0, 0.0, 2.0, 1.0))

        foo3 = foo3 * foo2.mat
        self.assertEqual(foo3, Vector4d(0.0, -2.0, 0.0, 1.0))

        #///////////////////////////////////////////__mul__ matrix44 Rotx * Roty * Rotz
        foo1 = Vector4d(2.0, 0.0, 0.0, 1.0)
        foo2 = Transform.create_rot_x(math.radians(90))
        foo3 = Transform.create_rot_y(math.radians(90))
        foo4 = Transform.create_rot_z(math.radians(90))

        foo5 = foo2 * foo3 * foo4
        foo6 = foo1 * foo5.mat
        foo7 = Vector4d(0.0, 0.0, -2.0, 1.0)
        self.assertEqual(foo6, foo7)

        #///////////////////////////////////////////__mul__ matrix44 Tr * Rotz
        foo1 = Vector4d(0.0, 0.0, 0.0, 1.0)
        foo2 = Transform.create_translate(1.0, 0.0, 0.0)
        foo4 = Transform.create_rot_z(math.radians(90))

        foo5 = foo1 * foo2 * foo4

        foo7 = Vector4d(0.0, 1.0, 0.0, 1.0)

        self.assertEqual(foo5, foo7)

    def test_mul_transform(self):

        #=========================================== Vector4 * transform(tr)
        foo1 = Vector4d(0.0, 0.0, 0.0, 1.0)
        foo2 = Transform.create_translate(1.0, 2.0, 3.0)
        foo3 = foo1 * foo2

        self.assertEqual(foo3.x, 1.0)
        self.assertEqual(foo3.y, 2.0)
        self.assertEqual(foo3.z, 3.0)

        #=========================================== Vector4 * transform(rtZ 90)
        foo1 = Vector4d(0.0, 1.0, 0.0, 1.0)
        foo2 = Transform.create_rot_z(math.radians(90))
        foo3 = foo1 * foo2

        self.assertEqual(foo3, Vector4d(-1.0, 0.0, 0.0, 1.0))
