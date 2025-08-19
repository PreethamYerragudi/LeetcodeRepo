# Problem 2348: Number of Zero-Filled Subarrays
# Difficulty: Medium
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = 0
        ans = 0
        for num in nums:
            if num == 0:
                n += 1
            elif num:
                ans += int((n * (n + 1)) / 2)
                n = 0
        if n:
            ans += int((n * (n + 1)) / 2)
        return ans



        