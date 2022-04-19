from Suit import Suit
from Value import Value
from Card import Card
import random


class Deck:

    __cardList = []

    def __init__(self):
        for s in Suit:
            for v in Value:
                self.__cardList.append(Card(s, v))

    def shuffle(self):
        random.shuffle(self.__cardList)

    def draw(self):
        return self.__cardList.pop()


