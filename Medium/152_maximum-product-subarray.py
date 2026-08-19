# Problem 152: Maximum Product Subarray
# Difficulty: Medium
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val, max_val = nums[0], nums[0]
        ans = max_val
        for i in range(1, len(nums)):
            pos = [nums[i], nums[i] * min_val, nums[i] * max_val]
            min_val = min(pos)
            max_val = max(pos)
            ans = max(ans, max_val)
        
        return ans
