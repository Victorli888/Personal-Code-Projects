from BlackJack import playingcards
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
    def __init__(self, deck):
        self.deck = deck
    money = 1000

    def draw(self, hand):
        rand_card = random.randint(0, len(deck))
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

    def display_hand(self,hand):  # Returns array with string values of card names & Total Value
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

        return f"{display_hand_arr}"

    def player_logic(self,value, hand):
        if value < 13:
            CPU1.draw(hand)
            return hand
        else:
            print("stand")





class Dealer(Player):

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
#
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



def cpu_logic(value, hand):
    if value < 13:
        CPU1.draw(hand)
        return hand
    else:
        print("stand")




def main():
    start = input("Black Jack with 3 players is about to start, to exit type quit")
    playing = True
    while playing:
        CPU1_hand = CPU1.deal_cards()
        CPU1_value = CPU1.calculate(CPU1_hand)
        if CPU1_value[0] == CPU1_value[1] or CPU1_value[1] > 21:
            CPU1_value.pop()

        current_hand = CPU1.display_hand(CPU1_hand)
        print(f"{current_hand} {CPU1_value}")
        CPU1_hand = cpu_logic(CPU1_value[0], CPU1_hand)
        print(CPU1_hand)
        playing = False


# Instatiate our players and dealer
CPU1 = Player(deck)
CPU2 = Player(deck)
Player1 = Player(deck)

main()