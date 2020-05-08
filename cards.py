import random

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        value_name = ""
        suit_name = ""
        if self.value == 0:
            value_name = "Two"
        elif self.value == 1:
            value_name = "Three"
        elif self.value == 2:
            value_name = "Four"
        elif self.value == 3:
            value_name = "Five"
        elif self.value == 4:
            value_name = "Six"
        elif self.value == 5:
            value_name = "Seven"
        elif self.value == 6:
            value_name = "Eight"
        elif self.value == 7:
            value_name = "Nine"
        elif self.value == 8:
            value_name = "Ten"
        elif self.value == 9:
            value_name = "Jack"
        elif self.value == 10:
            value_name = "Queen"
        elif self.value == 11:
            value_name = "King"
        elif self.value == 12:
            value_name = "Ace"

        if self.suit == 0:
            suit_name = "Spades"
        elif self.suit == 1:
            suit_name = "Clubs"
        elif self.suit == 2:
            suit_name = "Hearts"
        elif self.suit == 3:
            suit_name = "Diamonds"

        return value_name + " of " + suit_name

class StandardDeck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card(i,j)) for j in suits] for i in values]

    def shuffle(self):
        random.shuffle(self)
        print("\nDeck shuffled\n")

    def deal(self, location, times):
        for i in range(times):
            location.cards.append(self.pop(0))

    def burn(self):
        self.pop(0)

    def reset(self):
        self.clear()
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card(i,j)) for j in suits] for i in values]

deck = StandardDeck()
