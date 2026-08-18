# Problem 4010: Maximize Pair Strength Using GCD
# Difficulty: Easy
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        val = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                val = max(val, (nums[i] * nums[j]) // math.gcd(nums[i], nums[j]) ** 2)
        return val
            