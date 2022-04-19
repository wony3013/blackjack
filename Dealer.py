from Value import Value


class Dealer:
    __cards = []

    def __init__(self):
        self.__cards = []

    def recive_card(self, card):
        self.__cards.append(card)

    def get_score(self):
        score = 0
        acnt = []
        for card in self.__cards:
            if card.get_name() == Value.ACE.name:
                acnt.append(card)
            else:
                score += card.get_value()

        for i in acnt:
            if score > 10:
                score += 1
            else:
                score += 10
        return score

    def get_cards(self):
        hands = ''
        for card in self.__cards:
            hands += card.to_string()+" "
        return hands

