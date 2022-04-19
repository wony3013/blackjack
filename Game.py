from Deck import Deck
from Dealer import Dealer
from Player import Player

# 1차 리뷰
# - 게임, 룰 분리 필요, 좀더 OOP에 맞춰서
# - Player, Dealer 구분 없이 Deck으로 구분 하는것이 더 깔끔해보임
# - 덱에서 카드 다 뽑았을때 에러남
class Game:

    def start(self):

        dealer = Dealer()
        player = Player()

        print('Game Start! [Black Jack]')

        round = True #나중에 룰로 처리

        deck = Deck()
        print('Deck shuffling...')
        deck.shuffle()

        player.recive_card(deck.draw())
        player.recive_card(deck.draw())
        print(player.get_cards(), 'and Score :', player.get_score())

        opencard = deck.draw()
        print("Dealer Hand :", opencard.to_string(), "and [HIDDEN]")
        dealer.recive_card(opencard)
        dealer.recive_card(deck.draw())


        ip = ''

        while ip != '2':
            ip = input("draw? - Yes(1), No(2) :")
            if ip == '1':
                player.recive_card(deck.draw())
                print('Your Hand :', player.get_cards(), 'and Score :',
                      player.get_score())

                if player.get_score() > 21:
                    print("Bust, and Your Score :", player.get_score())
                    round = False
                    break

        print('Dealer card open !')
        print('Dealer Hand :', dealer.get_cards(), 'and Score :',
              dealer.get_score())
        while dealer.get_score() < 17:
            dealer.recive_card(deck.draw())
            print('Dealer Hand :', dealer.get_cards(), 'and Score :',
                  dealer.get_score())

            if dealer.get_score() > 21:
                print("Dealer Bust")
                break
        if round: #나중에 룰로 처리,
            if player.get_score() > dealer.get_score():
                print('[Player Win !!!!!]')
            elif player.get_score() == dealer.get_score():
                print('[Draw Game~]')
            else:
                print('[Dealer Win!!!!!]')
        else:
            print('[Dealer Win!!!!!]')


