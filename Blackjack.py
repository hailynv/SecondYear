from lab10_Answer_Key_MV import *
import random
import __future__

class BlackjackHand:
    # default constructor
    def __init__(self):
        self.playing_hand = []

    # adding a card to the playing hand list
    def add_card(self, new_card):
        self.playing_hand.append(new_card)

    # turning the hand into a string
    def __str__(self):
        current_hand = ""
        # iterating through the playing hand list
        for Card in self.playing_hand:
            # concatenating the Card string and the current_hand string
            current_hand = current_hand + Card.__str__() + ", "
        # removing the last whitespace and comma
        current_hand = current_hand[:-2]
        # return the finished string
        return current_hand

    def get_value(self):
        # variable declaration
        value = 0
        ace_count = 0
        # iterating through the playing hand list
        for Card in self.playing_hand:
            # counting aces here
            if Card.get_rank() == "Ace":
                ace_count = ace_count + 1
            # calculating the value as is with
            # aces having a value of 11
            value = value + Card.get_value()

        # some aces have a value of 1
        # this is where we adjust to make the best
        # hand possible
        while value > 21 and ace_count > 0:
            value = value - 10
            ace_count = ace_count - 1

        return value  # returning the value of the hand


# o lawd its blackjack
class Blackjack:
    # default constructor
    def __init__(self, starting_dollars):
        # creating a bank
        self.bank = ChipBank(starting_dollars)
        # making the deck list
        self.deck = []
        # making one of each card and adding it to
        # the deck list
        for index in range(52):
            card = Card(index)
            self.deck.append(card)
        # shuffling the cards
        random.shuffle(self.deck)

        # variable declarations
        self.player_hand = None
        self.dealer_hand = None
        self.wager = 0
        self.active_game = True

    def draw(self):
        # if the deck is empty we make a new one
        if len(self.deck) == 0:
            for index in range(52):
                card = Card(index)
                self.deck.append(card)
            random.shuffle(self.deck)

        # pulling from the end of the deck list
        index = len(self.deck)
        # index - 1 so we don't fall out of bounds
        card = self.deck[index - 1]
        # turning the card face up
        card.face_up()
        # deleting the card from the deck list
        del self.deck[index - 1]
        # returning the card pulled
        return card

    def start_hand(self, wager):
        # so many variables
        self.wager = wager
        self.player_hand = BlackjackHand()
        self.dealer_hand = BlackjackHand()
        self.active_game = True

        # adding two cards to the player's hand
        # calls the draw() function
        self.player_hand.add_card(self.draw())
        self.player_hand.add_card(self.draw())

        # dealer's first card has to be face down
        face_down_card = self.draw()
        # turning dealer's first card face down
        face_down_card.face_down()

        # adding two cards to the dealer's hand
        self.dealer_hand.add_card(face_down_card)
        self.dealer_hand.add_card(self.draw())

        # adjusting the value of the bank
        self.bank._value = self.bank._value - wager

        # printing the starting hands
        print("Your starting hand: {}".format(self.player_hand))
        print("Dealer's starting hand: {}".format(self.dealer_hand))

        # if the player's hand equals 21 and the
        # dealer's doesn't
        if self.player_hand.get_value() == 21 and\
                self.dealer_hand.get_value() != 21:
            print("You win, dealer loses!")
            # ending the round
            self.end_hand("win")
        # if the player's hand equals 21 and the
        # dealer's does too
        elif self.player_hand.get_value() == 21 and\
                self.dealer_hand.get_value() == 21:
            print("Tie!")  # aka a push but whatevs
            # ending the hand
            self.end_hand("push")
        # if the player's hand doesn't equal 21 and the
        # dealer's does
        elif self.player_hand.get_value() != 21 and\
                self.dealer_hand.get_value() == 21:
            print("Dealer wins, you lose!")
            self.end_hand("lose")  # ending the hand

    # taking a card out of the deck and adding it to the
    # player's hand
    def hit(self):
        # drawing a card
        drawn_card = self.draw()
        # adding to the player's hand
        self.player_hand.add_card(drawn_card)
        # printing what card was drawn and the updated
        # hand
        print("You draw a {}!".format(drawn_card))
        print("Your hand is now {}".format(self.player_hand))

        # checking the value of the player's hand
        # if it's > 21, player loses
        if self.player_hand.get_value() > 21:
            print("You bust, dealer wins!")
            self.end_hand("lose")  # ending the hand
        # if the player hits 21 exactly
        elif self.player_hand.get_value() == 21:
            self.stand()  # ending the hand

    # if a player chooses to keep their hand as is
    def stand(self):
        # the dealer's first card is flipped face up
        self.dealer_hand.playing_hand[0].face_up()
        # showing the dealer's hand
        print("Dealer's hand: {}".format(self.dealer_hand))
        # if the dealer's hand = 16, or if it's > than 16,
        # the dealer will keep hitting the deck
        while self.dealer_hand.get_value() <= 16:
            added_card = self.draw()  # drawing a card
            # adding the card to the dealer's hand
            self.dealer_hand.add_card(added_card)

            # printing what card was pulled and the
            # updated dealer hand
            print("Dealer draws {}".format(added_card))
            print("Dealer's hand is now {}".format(self.dealer_hand))

        # if the dealer's hand is > 21, they lose
        if self.dealer_hand.get_value() > 21:
            print("Dealer busts, you win!")
            self.end_hand("win")  # ending the hand
            return  # quitting the function

        # determining the winner
        # if the dealer's hand > player's hand, the dealer wins
        if self.dealer_hand.get_value() > self.player_hand.get_value():
            print("Dealer wins, you lose!")
            self.end_hand("lose")
        # if the dealer's hand < player's hand, the player wins
        elif self.dealer_hand.get_value() < self.player_hand.get_value():
            print("Player wins, dealer loses!")
            self.end_hand("win")
        # if the dealer's hand = player's hand, it's a push
        elif self.dealer_hand.get_value() == self.player_hand.get_value():
            print("Tie!")  # or a push but whatever
            self.end_hand("push")

    # if a winner has been determined this function is called
    def end_hand(self, outcome):
        # if the player wins, they get twice their wager back
        if outcome == "win":
            self.bank._value = self.bank._value + (2 * int(self.wager))
        # if it's a tie, the player gets their wager back
        elif outcome == ("push"):
            self.bank._value = self.bank._value + int(self.wager)
        # if a player loses nothing happens to their bank

        # reseting variables to None
        self.wager = None
        self.player_hand = None
        self.dealer_hand = None
        self.active_game = False

    # returns status of the game
    def game_active(self):
        return self.active_game


# TEST THINGS #
def main():
    blackjack = Blackjack(250)
    while blackjack.bank._value > 0:
        print("Your remaining chips: {}".format(blackjack.bank))
        wager = int(input("How much would you like to wager? "))
        blackjack.start_hand(wager)
        while blackjack.game_active():
            choice = raw_input("STAND or HIT: ").upper()
            if choice == "STAND":
                blackjack.stand()
            elif choice == "HIT":
                blackjack.hit()
        print("")
    print("Out of money! The casino wins!")


if __name__ == "__main__":
    main()
