from card import Card, Rank, Suit
from deck import Deck
from collections import Counter

class HandEvaluator:
    
    def evaluate(self, hand):
        sorted_hand = sorted(hand, key=lambda x: x.rank.value)
        
        ranks = [c.rank.value for c in sorted_hand]
        suits = [c.suit for c in sorted_hand]
        
        is_flush = len(set(suits)) == 1
        
        is_straight = all(ranks[i] == ranks[i-1] + 1 for i in range(1, len(ranks)))
        
        count = sorted(Counter(ranks).values(), reverse=True)
        
        is_fiveoak = count[0] == 5 # first value of count should be 5
        is_full_house = len(count) == 2 and count[0] == 3 and count[1] == 2
        is_fouroak = count[0] == 4
        is_threeoak = count[0] == 3
        is_two_pair = len(count) > 2 and count[0] == 2 and count[1] == 2
        is_pair = count[0] == 2

        if is_flush and is_fiveoak: return "Flush Five"
        if is_flush and is_full_house: return "Flush House"
        if is_fiveoak: return "Five of a Kind"
        if is_flush and is_straight: return "Straight Flush"
        if is_fouroak: return "Four of a Kind"
        if is_full_house: return "Full House"
        if is_flush: return "Flush"
        if is_straight: return "Straight"
        if is_threeoak: return "Three of a Kind"
        if is_two_pair: return "Two Pair"
        if is_pair: return "Pair"
        return "High Card"
    

# somewhat Auto-generated Test cases
def test_evaluator():
    evaluator = HandEvaluator()
    
    # Test Case: Full House (Aces and Kings)
    fh_hand = [
        Card(Rank.ACE, Suit.SPADES), Card(Rank.ACE, Suit.HEARTS), Card(Rank.ACE, Suit.CLUBS),
        Card(Rank.KING, Suit.DIAMONDS), Card(Rank.KING, Suit.SPADES)
    ]
    assert evaluator.evaluate(fh_hand) == "Full House"
    
    # Test Case: Straight Flush
    sf_hand = [Card(Rank(i), Suit.CLUBS) for i in range(2, 7)]
    assert evaluator.evaluate(sf_hand) == "Straight Flush"
    
    ff_hand = [Card(Rank.TWO, Suit.CLUBS), Card(Rank.TWO, Suit.CLUBS), Card(Rank.TWO, Suit.CLUBS), Card(Rank.TWO, Suit.CLUBS), Card(Rank.TWO, Suit.CLUBS)]
    assert evaluator.evaluate(ff_hand) == "Flush Five"
    
    fiveoak_hand = [Card(Rank.TWO, Suit.HEARTS), Card(Rank.TWO, Suit.CLUBS), Card(Rank.TWO, Suit.CLUBS), Card(Rank.TWO, Suit.CLUBS), Card(Rank.TWO, Suit.CLUBS)]
    assert evaluator.evaluate(fiveoak_hand) == "Five of a Kind"
    
    flushouse_hand = [
        Card(Rank.ACE, Suit.SPADES), Card(Rank.ACE, Suit.SPADES), Card(Rank.ACE, Suit.SPADES),
        Card(Rank.KING, Suit.SPADES), Card(Rank.KING, Suit.SPADES)
    ]
    assert evaluator.evaluate(flushouse_hand) == "Flush House"
    
    print("All specific tests passed!")
    
    
test_evaluator()