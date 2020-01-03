import random

class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val

    def show(self, name):
        self.name = name
        z =("{} of {}".format(self.value, self.suit))
        print(f"{self.name} Drew " + z)

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
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


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show(self.name)


deck = Deck()
deck.shuffle()

vic = Player("Victor")
vic.draw(deck)
vic.showHand()



cpu = Player("CPU")
cpu.draw(deck)
cpu.showHand()


