import random

SUITS = ["heart", "diamond", "spade", "club"]
FACES = ["jack", "queen", "king", "ace"]

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class CardDeck():
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.deck = []
        for s in SUITS:
            for r in range(2, 11):
                card = Card(str(r), s)
                self.deck.append(card)
            for f in FACES:
                card = Card(f, s)
                self.deck.append(card)
        
        random.shuffle(self.deck)

    def draw(self) -> Card:
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            print("Deck empty.  Starting new deck.")
            self.shuffle()
            return self.deck.pop()
        
# test = CardDeck()
# for i in range(0, 10):
#     t = test.draw()
#     print(f"card drawn: {t.value} of {t.suit}")