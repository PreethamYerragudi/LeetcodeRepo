# Problem 575: Distribute Candies
# Difficulty: Easy
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        types = len(set(candyType))
        return min(n // 2, types)