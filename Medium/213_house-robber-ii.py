# Problem 213: House Robber II
# Difficulty: Medium
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [-1] * len(nums)

        def dep(house, n):
            if house >= n:
                return 0
            if dp[house] != -1:
                return dp[house]
            dp[house] = max(nums[house] + dep(house + 2, n), dep(house + 1, n))
            return dp[house]

        first = dep(0, n - 1)
        dp = [-1] * len(nums)
        second = dep(1, n)
        return max(first, second)
