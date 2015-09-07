#-*- encoding: cp932
import card

class Deck:
    def __init__(self, max_cards):
        self.__max_cards = max_cards
        self.ssrs = []
        self.srs = []
        self.rs = []

    def total(self):
        return len(self.ssrs) + len(self.srs) + len(self.rs)

    def insert(self, cards):
        if self.total() > self.__max_cards:
            raise ArgumentError, "can't insert cards, too many cards in this deck."

        for card in cards:
            if card.rarity == "SSRare":
                self.ssrs.append(card)
            elif card.rarity == "SRare":
                self.srs.append(card)
            elif card.rarity == "Rare":
                self.rs.append(card)

    def skillup(self):
        pass
