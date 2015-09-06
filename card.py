#-*- encoding: cp932

class Card:
    def __setNeedPoint(self):
        if self.rarity == "SSRare":
            return self.skill_level * 4 * 2
        elif self.rarity == "SRare":
            return self.skill_level * 4
        elif self.rarity == "Rare":
            return self.skill_level * 2

    def __judgeLvup(self, cards):
        total = 0
        for card in cards:
            total += card.point

        if total >= self.need_point:
            return True
        return False

    def __init__(self, rarity, base_point):
        self.skill_level = 1
        self.rarity = rarity
        self.base_point = base_point
        self.need_point = self.__setNeedPoint()
        self.point = self.skill_level * self.base_point

    def skillup(self, cards):
        if self.__judgeLvup(cards):
            self.skill_level += 1
            self.need_point = self.__setNeedPoint()
            self.point = self.skill_level * self.base_point
            return True
        return False

class SSRare(Card):
    def __init__(self):
        Card.__init__(self, "SSRare", 40)

class SRare(Card):
    def __init__(self):
        Card.__init__(self, "SRare", 4)

class Rare(Card):
    def __init__(self):
        Card.__init__(self, "Rare", 1)
