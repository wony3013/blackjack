from Suit import Suit
from Value import Value
from Card import Card
import random


class Deck:

    __cardList = []

    def __init__(self):
        for s in Suit:
            for v in Value:
                print("suit : ", s, "value : ", v)
                self.__cardList.append(Card(s, v))

    def shuffle(self):
        random.shuffle(self.__cardList)

    def get_deck(self):
        return self.__cardList
