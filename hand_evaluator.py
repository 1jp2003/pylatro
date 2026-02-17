from card import Card, Rank, Suit

class HandEvaluator:
    
    @staticmethod
    def freq_check(ranks, suits):
        _dict = {}
        for card in ranks:
            _dict[card] = ranks.count(card)
        print(_dict)
        return _dict
    
    @staticmethod
    def evaluate(hand):
        sorted_hand = sorted(hand, key=lambda x: x.rank.value)
        
        ranks = [c.rank.value for c in sorted_hand]
        suits = [c.suit for c in sorted_hand]
        
        is_flush = len(set(suits)) == 1
        
        is_straight = all(ranks[i] == ranks[i-1] + 1 for i in range(1, len(ranks)))
        
        HandEvaluator.freq_check(ranks, suits)


        if is_flush and is_flush_five: return "Flush Five"
        if is_flush and is_full_house: return "Flush House"
        if is_fiveoak: return "Five of a Kind"
        if is_flush and is_straight: return "Straight Flush"
        if is_flush: return "Flush"
        if is_straight: return "Straight"
        if is_full_house: return "Full House"
        if is_threeoak: return "Three of a  Kind"
        return "High Card"
    

# --- Testing ---
# Correctly initializing a Flush of Spades

test_hand = [
    Card(Rank.TWO, Suit.SPADES),
    Card(Rank.THREE, Suit.SPADES),
    Card(Rank.FOUR, Suit.SPADES),
    Card(Rank.FIVE, Suit.SPADES),
    Card(Rank.SIX, Suit.SPADES)
]

test_hand = [
    Card(Rank.TWO, Suit.SPADES),
    Card(Rank.TWO, Suit.SPADES),
    Card(Rank.FOUR, Suit.SPADES),
    Card(Rank.FIVE, Suit.SPADES),
    Card(Rank.SIX, Suit.SPADES)
]

result = HandEvaluator.evaluate(test_hand)
print(f"Hand result: {result}")