#-*- encoding: utf-8

class Wallet:
    def __init__(self):
        self.total = 0

    def withdraw(self, times):
        self.total += times * 300
        return self.total
