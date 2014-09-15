from unittest import TestCase
from maths.vector2d import Vector2d


class TestVector2d(TestCase):

    def test_setZero(self):
        foo = Vector2d(1.0, 2.0)
        foo.set_to_zero()
        self.assertEqual(foo.x, 0.0)
        self.assertEqual(foo.y, 0.0)

    def test_dot(self):
        foo1 = Vector2d(1.0, 2.0)
        foo2 = Vector2d(10.0, 20.0)
        foo3 = foo1.dot(foo2)
        self.assertEqual(foo3, foo1.x * foo2.x + foo1.y * foo2.y)
