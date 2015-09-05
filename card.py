#-*- encoding: cp932

class Rarity:
    SSRare = 0
    SRare = 1
    Rare = 2

class Card:
    def __init__(self, rarity):
        self.skill_level = 1
        self.rarity = rarity

class SSRare(Card):
    def __init__(self):
        Card.__init__(self, "SSRare")
