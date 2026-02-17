from src.card import Card, Rank, Suit
from src.hand_evaluator import HandEvaluator
from src.deck import Deck
from src.scoring import ScoringEngine

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
    
def test_scoring_with_planets():
        # 1. Initialize the engine with your hard-coded stats
        engine = ScoringEngine()
        
        # 2. Test Level 1 Base Score
        chips_l1, mult_l1 = engine.calculate_base_score("Straight")
        assert (chips_l1, mult_l1) == (30, 4)
        
        # 3. Simulate using a Planet Card (Saturn)
        engine.level_up("Straight") # Now Level 2
        engine.level_up("Straight") # Now Level 3
        
        # 4. Verify the math for Level 3
        # Calculation: 30 + (2 * 30) = 90 Chips | 4 + (2 * 3) = 10 Mult
        chips_l3, mult_l3 = engine.calculate_base_score("Straight")
        
        assert chips_l3 == 90
        assert mult_l3 == 10
        print("✅ Planet Level-Up test passed!")
    
test_evaluator()
test_scoring_with_planets()


