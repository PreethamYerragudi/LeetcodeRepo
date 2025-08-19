# Problem 2214: Minimum Health to Beat Game
# Difficulty: Medium
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_val = max(damage)
        damage[damage.index(max_val)] = max_val - min(max_val, armor)
        return sum(damage) + 1