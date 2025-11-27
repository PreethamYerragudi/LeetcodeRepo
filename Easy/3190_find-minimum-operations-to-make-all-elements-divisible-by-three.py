# Problem 3190: Find Minimum Operations to Make All Elements Divisible by Three
# Difficulty: Easy
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans += min(3 - (num % 3), num % 3)
        return ans