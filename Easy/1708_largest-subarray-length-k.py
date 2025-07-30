# Problem 1708: Largest Subarray Length K
# Difficulty: Easy
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        num = max(nums[:len(nums) - k + 1])
        idx = nums.index(num)
        return nums[idx:idx+k]