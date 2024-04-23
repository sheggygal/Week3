import random

class DeckOfCards:
    def __init__(self):
        self.cards = []
        self.reset_deck()

    def reset_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            print("No cards left in the deck.")
            return None
        else:
            return self.cards.pop()

# Example usage:
deck = DeckOfCards()
print("Before shuffling:", deck.cards)
deck.shuffle()
print("After shuffling:", deck.cards)
print("Dealt card:", deck.deal())
print("Remaining cards:", deck.cards)
