class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits = ["Spade", "Heart", "Diamond", "Club"]

deck = [Card(value, suit) for value in range values, for suit in range suits]

card.value
