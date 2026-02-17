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
        self.current_bonus = 0 
        # For 'perishable' or 'probability' Jokers (like Gros Michel)
        self.is_active = True 
        # For 'eternal' stickers
        self.can_be_sold = sticker != Sticker.ETERNAL
        self.sell_value = 0
        self.buy_value = 0
    
    # when a card is triggered / played in hand 
    # photo, chad, hiker, etc 
    def on_card_scored(self):
        return
    
    # when the full hand is selected
    # before on_card_scored
    # vampire, midas, duo, trio? 
    def on_hand_scored(self):
        return
    
    # when the round is over (before cash out)
    # Mime, golden joker, 
    def on_blind_end(self):
        return
    
    # When the round starts
    # cartomancer, marble joker
    def on_blind_begin(self):
        return
    
    # When a pack is opened
    # Hallucination
    def on_pack_open(self):
        return
    
    # red card???
    def on_pack_close(self):
        return
    
    # Trading card, yorick 
    def on_card_discard(self):
        return
    
    def on_sell(self):
        return
    
    def get_retriggers(self):
        return 0
    
    def get_edition_bonus(self):
        if self.edition == Edition.FOIL: return 50, 0, 1.0   # +50 Chips
        if self.edition == Edition.MULT: return 0, 10, 1.0   # +10 Mult
        if self.edition == Edition.POLY: return 0, 0, 1.5    # x1.5 Mult
        return 0, 0, 1.0