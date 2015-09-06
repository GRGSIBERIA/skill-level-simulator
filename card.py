#-*- encoding: cp932

class Card:
    def __init__(self, rarity, point):
        self.skill_level = 1
        self.rarity = rarity
        self.point = point

    def skillup(self):
        self.skill_level += 1
        if self.rarity == "SSRare":
            self.point = self.skill_level * 4 * 2
        elif self.rarity == "SRare":
            self.point = self.skill_level * 4
        else:
            self.point = self.skill_level

class SSRare(Card):
    def __init__(self):
        Card.__init__(self, "SSRare", 40)

class SRare(Card):
    def __init__(self):
        Card.__init__(self, "SRare", 4)

class Rare(Card):
    def __init__(self):
        Card.__init__(self, "Rare", 1)
