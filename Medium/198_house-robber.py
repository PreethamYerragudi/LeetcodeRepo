# Problem 198: House Robber
# Difficulty: Medium
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def rob_all(curr):
            if curr >= len(nums):
                return 0
            if dp[curr] != -1:
                return dp[curr]
            ans = max(rob_all(curr + 1), rob_all(curr + 2) + nums[curr])
            dp[curr] = ans
            return ans
        return rob_all(0)
            