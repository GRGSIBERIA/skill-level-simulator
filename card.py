#-*- encoding: cp932

class Card:
    def __init__(self, rarity, base_point):
        self.skill_level = 1
        self.rarity = rarity
        self.base_point = base_point
        self.point = base_point

    def skillup(self):
        self.skill_level += 1
        self.point = self.skill_level * self.base_point

class SSRare(Card):
    def __init__(self):
        Card.__init__(self, "SSRare", 40)

class SRare(Card):
    def __init__(self):
        Card.__init__(self, "SRare", 4)

class Rare(Card):
    def __init__(self):
        Card.__init__(self, "Rare", 1)
