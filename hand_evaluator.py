from card import Card, Rank, Suit
from deck import Deck
from collections import Counter

class HandEvaluator:
    
    def _process_hand(self, hand):
        sorted_hand = sorted(hand, key=lambda x: x.rank.value)
        ranks = [c.rank.value for c in sorted_hand]
        suits = [c.suit for c in sorted_hand]
        count = sorted(Counter(ranks).values(), reverse=True)
        return ranks, suits, count
    
    def _is_straight(self, ranks):
        if ranks == [2,3,4,5,14]: # check for Ace straight
            return True
        else:
            return all(ranks[i] == ranks[i-1] + 1 for i in range(1, len(ranks))) 
    
    def _is_flush(self, suits):
        return len(set(suits)) == 1
    
    def _is_strush(self, suits, ranks): # straight flush
        return self._is_straight(ranks) & self._is_flush(suits)
    
    def _is_fiveoak(self, count):
        return count[0] == 5 # first value of count should be 5
    
    def _is_full_house(self, count):
        return len(count) == 2 and count[0] == 3 and count[1] == 2
    
    def _is_fouroak(self,count):
        return count[0] == 4
    
    def _is_threeoak(self,count):
        return count[0] == 3
    
    def _is_pair(self,count):
        return count[0] == 2

    def _is_two_pair(self, count):
        return len(count) > 2 and count[0] == 2 and count[1] == 2
    
    def evaluate(self, hand):
        ranks, suits, count = self._process_hand(hand=hand)
        
        is_flush = self._is_flush(suits=suits)
        
        is_straight = self._is_straight(ranks=ranks)
        
        is_straight_flush = self._is_strush(suits=suits, ranks=ranks)
        is_fiveoak = self._is_fiveoak(count=count)
        is_full_house = self._is_full_house(count=count)
        is_fouroak = self._is_fouroak(count=count)
        is_threeoak = self._is_threeoak(count=count)
        is_two_pair = self._is_two_pair(count=count)
        is_pair = self._is_pair(count=count)
        
        if is_flush and is_fiveoak: return "Flush Five"
        if is_flush and is_full_house: return "Flush House"
        if is_fiveoak: return "Five of a Kind"
        if is_straight_flush: return "Straight Flush"
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
    
    acestraight_hand = [
        Card(Rank.ACE, Suit.SPADES), Card(Rank.TWO, Suit.HEARTS), Card(Rank.THREE, Suit.CLUBS),
        Card(Rank.FOUR, Suit.DIAMONDS), Card(Rank.FIVE, Suit.SPADES)
    ]
    result = evaluator.evaluate(hand=acestraight_hand)
    print(result)

    print("All specific tests passed!")
    
def stress_test(iterations=1000):
    evaluator = HandEvaluator()
    for _ in range(iterations):
        deck = Deck()
        deck.shuffle()
        hand = deck.draw(5)
        evaluator.evaluate(hand)
    print(f"Successfully processed {iterations} random hands.")
    
test_evaluator()
stress_test()


