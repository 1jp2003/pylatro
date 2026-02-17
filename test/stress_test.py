import random
import time
from src.hand_evaluator import HandEvaluator
from src.scoring import ScoringEngine
from src.deck import Deck

def stress_test_planets(iterations=100000):
    # 1. Setup
    engine = ScoringEngine()
    hand_names = list(engine.HAND_STATS.keys())
    
    print(f"Starting stress test with {iterations} planet upgrades...")
    start_time = time.time()

    # 2. Randomly level up hands many times
    for _ in range(iterations):
        target_hand = random.choice(hand_names)
        engine.level_up(target_hand)

    # 3. Verification Phase
    print("Verifying mathematical consistency at high levels...")
    for hand, level in engine.current_levels.items():
        stats = engine.HAND_STATS[hand]
        actual_chips, actual_mult = engine.calculate_base_score(hand)
        
        # Manually calculate expected values
        expected_chips = stats["chips"] + (level - 1) * stats["s_chips"]
        expected_mult = stats["mult"] + (level - 1) * stats["s_mult"]
        
        # Assertions to ensure math is perfect
        assert actual_chips == expected_chips, f"Chip mismatch for {hand} at level {level}"
        assert actual_mult == expected_mult, f"Mult mismatch for {hand} at level {level}"

    end_time = time.time()
    duration = end_time - start_time
    
    print(f"✅ Stress test passed in {duration:.4f} seconds.")
    print(f"Average time per operation: {(duration/iterations)*1000000:.2f} microseconds.")

def stress_test_hands(iterations=10000):
    evaluator = HandEvaluator()
    for _ in range(iterations):
        deck = Deck()
        deck.shuffle()
        hand = deck.draw(5)
        evaluator.evaluate(hand)
    print(f"Successfully processed {iterations} random hands.")
    
if __name__ == "__main__":
    stress_test_planets()
    stress_test_hands()