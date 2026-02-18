from enum import Enum, IntEnum

class Edition(Enum):
    FOIL = 1;
    MULT = 2;
    POLY = 3;
    NEGATIVE = 4;
    
class Sticker(Enum):
    RENTAL = 1;
    PERISHABLE = 2;
    ETERNAL = 3;

class Joker:
    def __init__(self, name=None, edition=None, sticker=None):
        self.name = name 
        self.edition = edition
        self.sticker = sticker
        # The internal value for scaling Jokers
        self.current_chip_bonus = 0 
        self.current_mult_bonus = 0 
        # For 'perishable' or 'probability' Jokers (like Gros Michel)
        self.is_active = True 
        # For 'eternal' stickers
        self.can_be_sold = sticker != Sticker.ETERNAL
        self.sell_value = 0
        self.buy_value = 0
    
    # when a card is triggered / played in hand 
    # photo, chad, hiker, etc 
    def on_card_scored(self, card, hand_name, is_played):
        return 0, 0, 1.0
    
    # when the full hand is selected
    # before on_card_scored
    # vampire, midas, duo, trio? 
    def on_hand_scored(self, hand_name, current_chips, current_mult):
        return 0, 0, 1.0
    
    # when the round is over (before cash out)
    # Mime, golden joker, 
    def on_blind_end(self, gamestate):
        return
    
    def post_hand(self, cards_played, gamestate):
        return
    # When the round starts
    # cartomancer, marble joker
    def on_blind_begin(self, gamestate):
        return
    
    # When a pack is opened
    # Hallucination
    def on_pack_open(self):
        return
    
    # red card???
    def on_pack_skip(self):
        return
    
    # Trading card, yorick 
    def on_card_discard(self):
        return
    
    # Invis / cola
    def on_sell(self):
        # add self.sell_value to money and check joker conditions
        return
    
    # should deal with retriggers played 
    def get_retriggers(self, card, hand_name, is_played):
        return 0
    
    def get_edition_bonus(self):
        if self.edition == Edition.FOIL: return 50, 0, 1.0   # +50 Chips
        if self.edition == Edition.MULT: return 0, 10, 1.0   # +10 Mult
        if self.edition == Edition.POLY: return 0, 0, 1.5    # x1.5 Mult
        return 0, 0, 1.0