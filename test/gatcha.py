#-*- encoding: utf-8
import unittest
import gatcha

class GatchaTest(unittest.TestCase):
    def setUp(self):
        self.g = gatcha.Gatcha()

    def test_twist1(self):
        c = self.g.twist1()
        if c.name == "SSRare":
            self.assertEqual(c.point, 40)
        elif c.name == "SRare":
            pass
        elif c.name == "Rare":
            pass
