# Problem 26: Remove Duplicates from Sorted Array
# Difficulty: Easy
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 1
        while j < len(nums):
            if nums[j] == nums[j - 1]:
                j += 1
                continue
            nums[i] = nums[j]
            j += 1
            i += 1
        return i 