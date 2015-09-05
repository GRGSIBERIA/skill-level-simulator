#-*- encoding: cp932

class Card:
    def __init__(self, rarity):
        self.skill_level = 1
        self.rarity = rarity

class SSRare(Card):
    def __init__(self):
        Card.__init__(self, "SSRare")

class SRare(Card):
    def __init__(self):
        Card.__init__(self, "SRare")

class Rare(Card):
    def __init__(self):
        Card.__init__(self, "Rare")
