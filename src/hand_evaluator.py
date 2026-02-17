from src.card import Card, Rank, Suit
from src.deck import Deck
from collections import Counter

class HandEvaluator:
    
    def _process_hand(self, hand):
        sorted_hand = sorted(hand, key=lambda x: x.rank.value)
        ranks = [c.rank.value for c in sorted_hand]
        suits = [c.suit for c in sorted_hand]
        count = sorted(Counter(ranks).values(), reverse=True)
        # Count is used to find if we have the same type of card in our hand,
        # for pairs / 3oak / 4oak / Full House / Flush House / 5oak / Flush 5 
        return ranks, suits, count
    
    def _is_straight(self, ranks):
        if ranks == [2,3,4,5,14]: # check for Ace straight
            return True
        else:
            return all(ranks[i] == ranks[i-1] + 1 for i in range(1, len(ranks))) 
    
    def _is_flush(self, suits):
        return len(set(suits)) == 1
    
    def _is_flush_five(self, suits, count):
        return self._is_flush(suits) & self._is_fiveoak(count)
    
    def _is_flush_house(self, suits, count):
        return self._is_full_house(count) & self._is_flush(suits)
    
    def _is_strush(self, suits, ranks): # straight flush
        return self._is_straight(ranks) & self._is_flush(suits)
    
    def _is_fiveoak(self, count):
        return count[0] == 5 
    
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
        
        is_flush_five = self._is_flush_five(suits=suits, count=count)
        is_flush_house = self._is_flush_house(suits=suits, count=count)
        is_fiveoak = self._is_fiveoak(count=count)
        is_straight_flush = self._is_strush(suits=suits, ranks=ranks)
        is_flush = self._is_flush(suits=suits)
        is_straight = self._is_straight(ranks=ranks)
        is_full_house = self._is_full_house(count=count)
        is_fouroak = self._is_fouroak(count=count)
        is_threeoak = self._is_threeoak(count=count)
        is_two_pair = self._is_two_pair(count=count)
        is_pair = self._is_pair(count=count)
        
        if is_flush_five: return "Flush Five"
        if is_flush_house: return "Flush House"
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
    

