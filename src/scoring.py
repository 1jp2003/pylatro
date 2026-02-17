class ScoringEngine:
    HAND_STATS = {
        "High Card":      {"chips": 5,  "mult": 1, "s_chips": 10, "s_mult": 1},
        "Pair":           {"chips": 10, "mult": 2, "s_chips": 15, "s_mult": 1},
        "Two Pair":       {"chips": 20, "mult": 2, "s_chips": 20, "s_mult": 1},
        "Three of a Kind": {"chips": 30, "mult": 3, "s_chips": 20, "s_mult": 2},
        "Straight":       {"chips": 30, "mult": 4, "s_chips": 30, "s_mult": 3},
        "Flush":          {"chips": 35, "mult": 4, "s_chips": 15, "s_mult": 2},
        "Full House":     {"chips": 40, "mult": 4, "s_chips": 40, "s_mult": 4},
        "Four of a Kind":  {"chips": 60, "mult": 7, "s_chips": 30, "s_mult": 3},
        "Straight Flush": {"chips": 100, "mult": 8, "s_chips": 40, "s_mult": 4},
        "Five of a Kind":  {"chips": 120, "mult": 12, "s_chips": 35, "s_mult": 3},
        "Flush House":    {"chips": 140, "mult": 14, "s_chips": 40, "s_mult": 4},
        "Flush Five":     {"chips": 160, "mult": 16, "s_chips": 50, "s_mult": 3},
    }
    
    def __init__(self):
        # Access the class attribute directly
        self.current_levels = {hand: 1 for hand in self.HAND_STATS.keys()}

    def calculate_base_score(self, hand_name):
        level = self.current_levels[hand_name]
        # Use the class attribute for the math
        stats = self.HAND_STATS[hand_name]
        
        chips = stats["chips"] + (level - 1) * stats["s_chips"]
        mult = stats["mult"] + (level - 1) * stats["s_mult"]
        return chips, mult
    
    def level_up(self, hand_name):
        self.current_levels[hand_name] += 1

    def calculate_final_score(self):
        return