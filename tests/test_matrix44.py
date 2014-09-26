from unittest import TestCase
import random
import math
from maths.matrix44 import Matrix44
from core.transform import  Transform


class TestMatrix44(TestCase):

    def test___sub__(self):
        foo0 = Matrix44()
        foo1 = Matrix44()
        foo2 = Matrix44()

        for i in range(0, 4):
            for j in range(0, 4):
                foo1[i][j] = random.random()
                foo2[i][j] = random.random()
                foo0[i][j] = foo1[i][j] - foo2[i][j]

        foo3 = foo1 - foo2

        for i in range(0, 4):
            for j in range(0, 4):
                self.assertEqual(foo3[i][j], foo0[i][j])

    def test___add__(self):
        foo0 = Matrix44()
        foo1 = Matrix44()
        foo2 = Matrix44()

        for i in range(0, 4):
            for j in range(0, 4):
                foo1[i][j] = random.random()
                foo2[i][j] = random.random()
                foo0[i][j] = foo1[i][j] + foo2[i][j]

        foo3 = foo1 + foo2

        for i in range(0, 4):
            for j in range(0, 4):
                self.assertEqual(foo3[i][j], foo0[i][j])

    def test__get_invert_by_transpose_(self):

        foo1 = Transform.create_rot_z(math.radians(90))
        foo2 = Transform.create_identity()

        foo3 = foo1.mat * foo1.mat_inv

        self.assertEqual(foo3, foo2.mat)

    def test__get_real_invert_(self):
        foo1 = Transform.create_translate(1.0,2.0,3.0)
        foo2 = foo1.mat.get_invert()

        self.assertEqual(foo2, foo1.mat_inv)

    def test__mat_invert_(self):
        foo1 = Transform.create_translate(10.0,2.0,3.0)
        foo2 = Transform.create_rot_x(math.radians(37))
        foo3 = Transform.create_translate(1.0,-2.0,-6.0)
        foo4 = Transform.create_rot_y(math.radians(7))
        foo5 = Transform.create_translate(1.0,7.0,2.0)
        foo6 = Transform.create_rot_z(math.radians(137))

        foo7 = foo1 * foo2 * foo3 * foo4 * foo5 * foo6

        self.assertEqual(foo7.mat.get_invert(), foo7.mat_inv)
        self.assertEqual(foo7.mat_inv, foo7.mat_inv)
