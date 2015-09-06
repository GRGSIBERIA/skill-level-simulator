#-*- encoding: cp932

class Card:
    def __setNeedPoint(self):
        if self.rarity == "SSRare":
            self.need_point = self.skill_level * 4 * 2
        elif self.rarity == "SRare":
            self.need_point = self.skill_level * 2
        elif self.rarity == "Rare":
            self.need_point = self.skill_level

    def __init__(self, rarity, base_point):
        self.skill_level = 1
        self.rarity = rarity
        self.base_point = base_point
        self.need_point = self.__setNeedPoint()

    def skillup(self):
        self.skill_level += 1
        self.need_point = self.__setNeedPoint()

class SSRare(Card):
    def __init__(self):
        Card.__init__(self, "SSRare", 40)

class SRare(Card):
    def __init__(self):
        Card.__init__(self, "SRare", 4)

class Rare(Card):
    def __init__(self):
        Card.__init__(self, "Rare", 1)
