# Problem 1365: How Many Numbers Are Smaller Than the Current Number
# Difficulty: Easy
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            temp = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    temp += 1
            ans[i] = temp
        return ans