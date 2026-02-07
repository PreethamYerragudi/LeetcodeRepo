# Problem 3010: Divide an Array Into Subarrays With Minimum Cost I
# Difficulty: Easy
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        i = nums[0]
        nums.pop(0)
        nums.sort()
        return sum(nums[0:2]) + i