#-*- encoding: cp932
import unittest
import gatcha

class Gatchatest(unittest.TestCase):
    def setUp(self):
        self.g = gatcha.Gatcha(3, 6)

    def __getRarity(self, rarity):
        while True:
            c = self.g.twist1()
            if c.rarity == rarity:
                return c

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

    def test_skillup_ssr(self):
        c = self.__getRarity("SSRare")
        e = [self.__getRarity("SRare")]
        self.assertEqual(c.skillup(e), False)
        self.assertEqual(c.skillup(e * 2), True)

        self.assertEqual(c.skillup(e * 4), True)
        self.assertEqual(c.skill_level, 3)
        self.assertEqual(c.need_point, 3 * 4 * 2)
        self.assertEqual(c.skillup(e * 6), True)
        self.assertEqual(c.skill_level, 4)

    def test_skillup_sr(self):
        c = self.__getRarity("SRare")
        e = [self.__getRarity("Rare")]
        self.assertEqual(c.skillup(e), False)
        self.assertEqual(c.skillup(e * 4), True)

    def test_skillup_r(self):
        c = self.__getRarity("Rare")
        e = [self.__getRarity("Rare")]
        self.assertEqual(c.skillup(e), False)
        self.assertEqual(c.skillup(e * 2), True)

    def test_skilluped(self):
        ssr = self.__getRarity("SSRare")
        sr = [self.__getRarity("SRare")]
        r = [self.__getRarity("Rare")]

        self.assertEqual(ssr.skillup(sr + r * 4), True)
        
        

if __name__ == '__main__':
    unittest.main()
