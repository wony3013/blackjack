class Card:

    __suit = None
    __value = None

    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    def get_suit(self):
        return self.__suit

    def get_value(self):
        return self.__value

    def to_string(self):
        return self.__suit.name + "(" + str(self.__suit.value) + ")-" \
               + self.__value.name + "(" + str(self.__value.value) + ")"