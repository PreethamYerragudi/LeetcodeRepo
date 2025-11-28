# Problem 485: Max Consecutive Ones
# Difficulty: Easy
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        temp = 0
        for val in nums:
            if val == 1:
                temp += 1
            else:
                ans = max(temp, ans)
                temp = 0
        ans = max(temp, ans)
        return ans