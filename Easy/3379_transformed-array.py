# Problem 3379: Transformed Array
# Difficulty: Easy
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [-1 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            if num == 0:
                result[i] = 0
            else:
                result[i] = (nums[(i + nums[i]) % len(nums)])
        
        return result