# Hashmap for full deck Card : Value

class Cards():

    # Generates desired number of decks of cards
    def generate(self, num_of_decks):
        """:cvar Input Number of decks of 52 Cards needed
        Each card is represented as a tuple defined by ( int card value, str card suit)
        generate() Returns array Deck; Array contains tuples where tuples are (card value, card suit)
        """
        deck = []

        for i in range(num_of_decks):
            for i in range (1,14):
                for j in ["Spade","Hearts","Diamond","Clubs"]:
                    deck.append((i,j))
        return deck






# Testing
# cards = Cards()  # Intialize class and create cards object
# deck = cards.generate(2)
#
# print(deck[66])


