#-*- encoding: cp932
import gatcha as g

if __name__ == '__main__':
    gat = g.Gatcha(3, 6)
    for c in gat.twist10():
        print c.rarity
