# Problem 34: Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        if l >= len(nums) or l < 0 or nums[l] != target:
            return [-1, -1]
        start = l
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        end = r
        return [start, end]