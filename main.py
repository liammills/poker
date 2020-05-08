from cards import deck
from players import Player

def main():

    deck.shuffle()
    print(len(deck))

    playerx = Player("Liam")
    deck.deal(playerx, 5)

    print(len(deck))
    print(playerx.cards)



if __name__ == "__main__":
    main()
