#-*- encoding: cp932
import unittest
import gatcha

class Gatchatest(unittest.TestCase):
    def setUp(self):
        self.g = gatcha.Gatcha(3, 6)

    def test_twist1(self):
        c = self.g.twist1()
        if c.rarity == "SSRare":
            self.assertEqual(c.point, 40)
        elif c.rarity == "SRare":
            self.assertEqual(c.point, 4)
        elif c.rarity == "Rare":
            self.assertEqual(c.point, 1)

    def test_twist10(self):
        cs = self.g.twist10()
        self.assertEqual(len(cs), 10)

if __name__ == '__main__':
    unittest.main()
