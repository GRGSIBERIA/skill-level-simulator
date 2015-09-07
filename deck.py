#-*- encoding: cp932
import card

class Deck:
    def __init__(self, max_cards):
        self.__max_cards = max_cards
        self.ssrs = []
        self.srs = []
        self.rs = []
        for i in range(10):
            self.ssrs.append([])
            self.srs.append([])
            self.rs.append([])

        self.waifu = None

    def __findCard(self, cards, c):
        for level in cards:
            for i in range(len(level))
                if level[i] == c:
                    del level[i]
                    return True
        return False

    def __appendForSkillLevel(self, c, func):
        if c.rarity == "SSRare":
            self.ssrs[func(c)].append(c)
        elif c.rarity == "SRare":
            self.srs[func(c)].append(c)
        elif c.rarity == "Rare":
            self.rs[func(c)].append(c)

    def __totalType(self, cards):
        total = 0
        for level in cards:
            total += len(level)
        return total

    def total(self):
        return self.__totalType(self.ssrs) + \
                self.__totalType(self.srs) + \
                self.__totalType(self.rs)

    def insert(self, cards):
        if self.total() > self.__max_cards:
            raise ArgumentError, "can't insert cards, too many cards in this deck."

       for c in cards:
           self.__appendForSkillLevel(c, lambda x: 0)

    def setWaifu(self, c):
        self.waifu = c
        if not self.__findCard(self.ssrs, c):
            if not self.__findCard(self.srs, c):
                if not self.__findCard(self.rs, c):
                    raise ArgumentError, "don't have selected waifu card."
        self.__appendForSkillLevel(c, lambda x: x.skill_level - 1)
