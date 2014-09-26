from unittest import TestCase
import math


class TestTransform(TestCase):
    def test__get_invert__(self):
        from core.transform import Transform

        foo0 = Transform.create_rot_z(math.radians(90))
        foo1 = Transform.create_identity()
        foo2 = foo0.get_invert()

        foo3 = foo0 * foo2

        self.assertEqual(foo3, foo1)

    def test_set_to_identity(self):
        from core.transform import Transform

        foo = Transform.create_identity()

        for i in range(0, 4):
            for j in range(0, 4):
                if i == j:
                    self.assertEqual(foo.mat[i][j], 1.0)
                    self.assertEqual(foo.mat_inv[i][j], 1.0)
                else:
                    self.assertEqual(foo.mat[i][j], 0.0)
                    self.assertEqual(foo.mat_inv[i][j], 0.0)

    def test___mul__(self):
        from core.transform import Transform
        from maths.matrix44 import Matrix44
        from maths.vector4d import Vector4d

        # //////////////////////////////////////////////////////I *I = I
        foo1 = Transform.create_identity()
        foo2 = Transform.create_identity()

        foo3 = foo1 * foo2

        for i in range(0, 4):
            for j in range(0, 4):
                if i == j:
                    self.assertEqual(foo3.mat[i][j], 1.0)
                    self.assertEqual(foo3.mat_inv[i][j], 1.0)
                else:
                    self.assertEqual(foo3.mat[i][j], 0.0)
                    self.assertEqual(foo3.mat_inv[i][j], 0.0)
        #//////////////////////////////////////////////////////Ta * Tb = Tab
        foo1 = Transform.create_translate(1.0, 0.0, 0.0)
        foo2 = Transform.create_translate(0.0, 2.0, 0.0)

        foo0 = foo1 * foo2

        for i in range(0, 3):
            for j in range(0, 4):
                if i == j:
                    self.assertEqual(foo3.mat[i][j], 1.0)
                else:
                    self.assertEqual(foo3.mat[i][j], 0.0)

        self.assertEqual(foo0.mat[3][0], 1.0)
        self.assertEqual(foo0.mat[3][1], 2.0)
        self.assertEqual(foo0.mat[3][2], 0.0)
        self.assertEqual(foo0.mat[3][3], 1.0)

        self.assertEqual(foo0.mat[3], Vector4d(1.0, 2.0, 0.0, 1.0))

        #//////////////////////////////////////////////////////RotXa * RotXb = RotXab
        foo0 = Transform.create_rot_x(math.radians(90))
        foo1 = Transform.create_rot_x(math.radians(45))
        foo2 = Transform.create_rot_x(math.radians(45))

        foo3 = foo1 * foo2

        self.assertEqual(foo0, foo3)

        #//////////////////////////////////////////////////////RotZ(a) * RotZ(-a) = I
        foo0 = Transform.create_rot_z(math.radians(90))
        foo1 = Transform.create_rot_z(math.radians(-90))

        foo2 = foo0 * foo1
        foo3 = Transform.create_identity()

        self.assertEqual(foo2, foo3)

        #//////////////////////////////////////////////////////Tr(a) * Tr(-a) = I
        foo0 = Transform.create_translate(1.0, 0.0, 0.0)
        foo1 = Transform.create_translate(-1.0, 0.0, 0.0)

        foo2 = foo0 * foo1
        foo3 = Transform.create_identity()

        self.assertEqual(foo2, foo3)

        #//////////////////////////////////////////////////////RotXa * T = RotXab
        foo0 = Transform.create_translate(1.0, 2.0, 3.0)
        foo1 = Transform.create_rot_x(math.radians(90))
        foo2 = Transform.create_rot_z(math.radians(22))
        foo3 = Transform.create_translate(1.0, 2.0, 3.0)

        foo4 = foo0 * foo1 * foo2 * foo3

        self.assertEqual(foo4.mat_inv, foo4.mat.get_invert())

    def test__look_at(self):
        from core.transform import Transform
        from maths.point3d import Point3d
        from maths.vector3d import Vector3d

        pos = Point3d(0.0, 0.0, 0.0)
        at = Point3d(0.0, 0.0, 1.0)
        up = Vector3d.get_up()

        t = Transform.create_look_at(pos, at, up)
