#-*- encoding: cp932
import card
import random

class Gatcha:
    def __init__(self, ssr_prob, sr_prob):
        self.ssr_prob = ssr_prob
        self.sr_prob = sr_prob

    def __getRandom(self):
        return random.uniform(0, 100)

    def twist1(self):
        choice = self.__getRandom()
        if choice > self.ssr_prob:
            return card.SSRare()
        elif choice > self.sr_prob:
            return card.SRare()
        return card.Rare()

    def twist10(self):
        retval = []
        for i in range(10):
            retval.append(self.twist1())
        return retval
