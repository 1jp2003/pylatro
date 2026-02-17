from enum import Enum, IntEnum

class Suit(Enum):
    SPADES = 1; HEARTS = 2; CLUBS = 3; DIAMONDS = 4

class Rank(IntEnum):
    TWO = 2;
    THREE = 3;
    FOUR = 4;
    FIVE = 5;
    SIX = 6;
    SEVEN = 7;
    EIGHT = 8;
    NINE = 9;
    TEN = 10;
    JACK = 11;
    QUEEN = 12;
    KING = 13;
    ACE = 14;
    
class Card:
    def __init__(self, rank, suit, edition=None, enhancement=None, seal=None):
        self.rank = rank
        self.suit = suit
        self.edition = edition      # "Polychrome"
        self.enhancement = enhancement # "Glass"
        self.seal = seal # "Red Seal"