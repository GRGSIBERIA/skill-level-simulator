#-*- encoding: cp932
import sys
import gatcha as g
import deck as d
import wallet as w

if __name__ == '__main__':
    MAX_CARDS = 40
    gatcha = g.Gatcha(3, 6)
    deck = d.Deck(MAX_CARDS)
    wallet = w.Wallet()
    end_flag = False

    while not end_flag:
        print "-----------------------------------"
        print "Deck: %s/%s" % (deck.total(), MAX_CARDS)
        print "Spend: %s yen" % (wallet.total)
        print ""
        print "command?"
        print "t1 : twist1"
        print "t10: twist10"
        print "u  : skillup"
        print "s  : status"
        print "q  : quit"
        command = raw_input()
        
        if command == "t1":
            wallet.withdraw(1)
            card = gatcha.twist1()
            deck.insert([card])

        elif command == "t10":
            try:
                wallet.withdraw(10)
                cards = gatcha.twist10()
                deck.insert(cards)
            except ArgumentError as e
                print e.message

        elif command == "u":
            deck.skillup()

        elif command == "s":
            pass

        elif command == "q":
            end_flag = True
