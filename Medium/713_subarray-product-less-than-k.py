# Problem 713: Subarray Product Less Than K
# Difficulty: Medium
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            while prod >= k and l <= r:
                prod /= nums[l]
                l += 1
            ans += r - l + 1
        return ans