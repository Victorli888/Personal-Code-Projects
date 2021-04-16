import playingcards
import random
"""
Features Needed:
- 6 people table
- Dealer that must hit until 17 or higher is reached
- 7 seperate Money values for dealer and players
- Button for Hit, Stand, Double Down  --- stand and double down adressed in main()
- INSURANCE NOT AVAILABLE (can be added later)
- 5 Shoe Black Jack when 75% of the deck is dealt re-shuffle the shoe
"""





class Player():
    def __init__(self, deck, name):
        self.deck = deck
        self.name = name
    money = 1000

    def draw(self, hand):
        rand_card = random.randint(0, len(deck)-1)
        hand.append(deck.pop(rand_card))
        return hand

    def deal_cards(self):
        hand = []
        for i in range(2):
            rand_card = random.randint(0, len(deck))
            hand.append(deck.pop(rand_card))
        return hand

    def calculate(self, hand): # Returns value Aces = 1 and Aces = 11  and other hands use 0th index
        total = [0, 0]

        for i in range(0, len(hand)):
            card_index = hand[i][0]

            if card_index > 10:  # Case 1: 11,12,13 Face Cards should be be valued at 10
                total[0] += 10
                total[1] += 10

            elif card_index == 1:  # If Ace we need to calculate both 1 and 11
                total[0] += 1
                total[1] += 11
            else:   # All other cases we simply add the value to hand
                total[0] += card_index
                total[1] += card_index


        return total

    def display_hand(self, hand):  # Returns array with string values of card names & Total Value
        card_name = {
            1: "Ace",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        display_hand_arr = []  # Cards to be shown to the player will be stored in this array (String)

        for i in range(0, len(hand)):
            card_value = hand[i][0]  # return Card index
            display_hand_arr.append(card_name[card_value])  # Reference card index and append card's name in hashmap

        return display_hand_arr

    def value_check(self, hand):

        value = self.calculate(hand)
        current_hand = self.display_hand(hand)
        value_show = value

        if "Ace" in value:
            value_show = value
        elif value[1] > value[0] and value[1] <= 21:
            value_show = value[1]
        elif value[0] == value[1]:
            value_show = value[1]

        print(f"{self.name}: {current_hand} {value_show}")

        if value[0] > 21:
            print("Bust")

        return value

    def turn(self):  # Method for CPU Turn
        hand = self.deal_cards()
        value = self.calculate(hand)

        while value[0] <= 15 or value[1] <= 15:

            hand = self.draw(hand)
            value = self.value_check(hand)



    def player_prompt(self):
        print("Would you like to (A) Hit (B) Stand")
        ans = input("> ")
        return ans

    def player_turn(self):  # We can optimize here by re-using logic from turn()
        hand = self.deal_cards()
        value = self.value_check(hand)


        ans = self.player_prompt()

        while ans == "A":
            hand = self.draw(hand)
            value = self.calculate(hand)
            current_hand = self.display_hand(hand)

            if value[1] > value[0] and value[1] <= 21:
                value.pop(0)
            if value[0] == value[1] or value[1] > 21:
                value.pop()
            print(f"{self.name}: {current_hand} {value}")
            if value[0] > 21:
                return print("Bust")  # needs to finish the game to dealer

            ans = self.player_prompt()
        # maybe we can put in a block of code to prevent invalid entries
        print("stand")


class Dealer(Player):
    def flop(self):
        dealer_hand = Dealer.deal_cards()
        dealer_curr_hand = Dealer.display_hand(dealer_hand)
        dealer_curr_hand.pop()
        dealer_curr_hand.append("Hidden")
        print(f"{Dealer.name}: {dealer_curr_hand}")





    dialogues = {
        "Lose": "Dealer Busts!",
        "Win": "Dealer Wins",
        "BJ": "Dealer got BlackJack!"
    }






"""
Test Cases
"""

cards = playingcards.Cards()  # Create playing cards
deck = cards.generate(5)  # Generates 5 Shoe Deck of Cards
# print(len(deck))

# CPU1 = Player(deck)
# CPU1_hand = CPU1.deal_cards()  # Deal the cards
# CPU1_hand = CPU1.draw(CPU1_hand)  # Draw a Card command: HIT
# CPU1_hand_total = CPU1.calculate(CPU1_hand)  # Calculate amount for game
# CPU1_display_hand = CPU1.display_hand(CPU1_hand)  # Display card_names to player
#
#
# print(CPU1_hand)
# print(len(deck))
# print(CPU1_display_hand)
# print(CPU1_hand_total)



def main():
    # start = input("Black Jack with 3 players is about to start, to exit type quit")
    playing = True
    while playing:
        Dealer.flop()
        CPU1.turn()
        CPU2.turn()
        Player1.player_turn()
        ans = input("Would you like to leave the table? (y/n)")
        if ans == "y":
            print("You have left...")
            playing = False
        else:
            print("Dealer is dealing cards!")









if __name__ == '__main__':
    # Instatiate our players and dealer
    print(len(deck))
    Dealer = Dealer(deck, "Dealer")
    CPU1 = Player(deck, "CPU1")
    CPU2 = Player(deck, "CPU2")
    Player1 = Player(deck, "Player1")

    main()