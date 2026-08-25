# Problem 3718: Smallest Missing Multiple of K
# Difficulty: Easy
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        for i in range(1, len(nums) + 2):
            if i * k not in seen:
                return i * k
        