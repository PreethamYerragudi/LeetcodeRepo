# Problem 268: Missing Number
# Difficulty: Easy
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums_set = set(nums)
        for x in range(n, -1, -1):
            if x not in nums_set:
                return x
        return -1
