from unittest import TestCase
import random
import math
from maths.matrix44 import Matrix44
from core.transform import  Transform

__author__ = 'nicolas'


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

    def test__get_invert__(self):

        foo1 = Transform.create_rot_z(math.radians(90))
        foo2 = Transform.create_identity()

        foo3 = foo1.mat * foo1.mat_inv

        self.assertEqual(foo3, foo2.mat)




