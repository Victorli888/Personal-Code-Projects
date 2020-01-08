import random

class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val

    def show(self, name):
        self.name = name
        z = ("{} of {}".format(self.value, self.suit))
        print(f"{self.name} Drew " + z)

    def display(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()


    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        '''
        :return: returning a random card
        '''
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def drawCard(self):

        '''
        take a card from the array and remove it from the list
        :return:
        '''
        return self.cards.pop()

    def display(self):
        for c in self.cards:
            c.display()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show(self.name)


deck = Deck()
deck.shuffle()

vic = Player("Victor")
for i in range (1, 6):
    vic.draw(deck)
vic.showHand()

cpu = Player("CPU")
for i in range (1, 6):
    cpu.draw(deck)
cpu.showHand()

deck.display()