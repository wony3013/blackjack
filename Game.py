from Deck import Deck
from Dealer import Dealer
from Player import Player
from Rule import Rule


class Game:
    rule = None

    def __init__(self):
        self.rule = Rule()

    def start(self):

        dealer = Dealer()
        player = Player()

        print('~~Black Jack~~ Game Start! ')

        deck = Deck()
        print('Deck shuffling...')
        deck.shuffle()

        player.recive_card(deck.draw())
        player.recive_card(deck.draw())
        print("Your Hand :", player.get_cards(), 'and Score :', player.get_score())

        dealer.recive_card(deck.draw())
        print("Dealer Hand :", dealer.get_cards(), "and [HIDDEN]")
        dealer.recive_card(deck.draw())

        ip = 0

        while ip != '2':
            ip = input("draw? - Yes(1), No(2) :")
            if ip == '1':
                player.recive_card(deck.draw())
                print('Your Hand :', player.get_cards(), 'and Score :', player.get_score())

                if self.rule.bust_check(player.get_score()):
                    print("Bust, and Your Score :", player.get_score())
                    break

        print('Dealer card open !')
        print('Dealer Hand :', dealer.get_cards(), 'and Score :', dealer.get_score())
        while self.rule.delear_draw_check(dealer.get_score()):
            print('Dealer draw a card and...')
            dealer.recive_card(deck.draw())
            print('Dealer Hand :', dealer.get_cards(), 'and Score :', dealer.get_score())

            if self.rule.bust_check(dealer.get_score()):
                print("Dealer Bust")
                break

        print(self.rule.end_game(player, dealer))


