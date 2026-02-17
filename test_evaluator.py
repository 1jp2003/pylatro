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
    
def stress_test(iterations=10000):
    evaluator = HandEvaluator()
    for _ in range(iterations):
        deck = Deck()
        deck.shuffle()
        hand = deck.draw(5)
        evaluator.evaluate(hand)
    print(f"Successfully processed {iterations} random hands.")
    
    
if __name__ == "main":
    test_evaluator()
    stress_test()


