# Problem 1464: Maximum Product of Two Elements in an Array
# Difficulty: Easy
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max((nums[0] - 1) * (nums[1] - 1), (nums[-1] - 1) * (nums[-2] - 1))