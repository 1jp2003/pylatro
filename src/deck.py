import random
from src.card import Card, Rank, Suit

class Deck:
    def __init__(self):
        # Create a standard 52-card deck using your Enums
        self.cards = [Card(r, s) for r in Rank for s in Suit]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self, n):
        # draw n cards from a deck
        hand = self.cards[:n]
        self.cards = self.cards[n:]
        return hand