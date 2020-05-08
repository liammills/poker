import time,sys
import pygame as pg
from cards import deck
from players import Player

class BlackjackPlayer(Player):
    def get_score(self):
        score = 0
        aces = 0
        for card in self.cards:
            if card.value < 8:
                score += card.value+2
            elif card.value < 12:
                score += 10
            else:
                aces += 1
        for ace in range(aces):
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        return score

    def __repr__(self):
        hand = ""
        for i in range(len(self.cards)):
            if i == len(self.cards)-1:
                hand+=str(self.cards[i])
            else:
                hand+=str(self.cards[i])+"    |    "
        return hand


def new_round():
    deck.reset()
    user.cards.clear()
    comp.cards = []

    # Shuffle deck
    deck.shuffle()
    time.sleep(0.4)

    # Deal deck
    deck.deal(user, 2)
    deck.deal(comp, 2)
    print("Deck dealt\n")

# Set up players
ipt = input("Enter your name: ")
user = BlackjackPlayer(ipt)
comp = BlackjackPlayer("Computer")
time.sleep(0.4)

chips = 100

# Set up pygame window
#pg.init()
#pg.display.set_caption('Mills Blackjack')
#clock = pg.time.Clock()
#fps=60
#pg.mouse.set_visible(0)
#screen = pg.display.set_mode((800, 600))

while True:
    new_round()

    print("You have "+str(chips)+" chips.")
    while True:
        bet = int(input("How much are you going to bet? "))
        if bet > 0 and bet <= chips:
            break
    round = True

    print("The house has a "+str(comp.cards[0])+"\n")

    while round is True:
        # Print updated player's hand
        print("\nYour hand:\n"+str(user))
        time.sleep(0.4)

        # Get user's turn
        ipt = input("\n\nHit, stay or fold? ")
        print()

        if ipt.lower() == "fold":
            print("Ok, game over.")
            round=False

        elif ipt.lower() == "hit":
            deck.deal(user,1)

        elif ipt.lower() == "stay":
            print("Playing out a round.\n")
            time.sleep(0.4)
            print("The house has: "+str(comp)+"\n")
            while comp.get_score() < 17:
                deck.deal(comp, 1)
                time.sleep(0.7)
                print("The house is dealt a "+str(comp.cards[len(comp.cards)-1]))
                time.sleep(0.2)
                print("House: "+str(comp)+"\n")
            time.sleep(0.7)
            print("Calculating...\n")
            time.sleep(1.5)
            print("The house had "+ str(comp.get_score())+".")
            time.sleep(0.4)
            print("You had "+str(user.get_score())+".")
            time.sleep(0.4)
            print()
            if comp.get_score() > 21:
                print("The house busts. Good job, "+user.name + ", you win "+str(bet)+"!")
                chips += bet
            elif comp.get_score() >= user.get_score() or user.get_score() > 21:
                print("The house wins.")
                chips -= bet
            elif user.get_score() > comp.get_score():
                print("Good job, "+user.name + ", you win "+str(bet)+"!")
                chips += bet
            time.sleep(0.4)
            if chips == 0:
                print("\nYou are out of chips. Game over :(")
                sys.exit(0)
            round=False

        else:
            print("Not a correct input.")

    ipt = input("Another round? (Y/N) ")
    if ipt.lower() == "n":
        break
