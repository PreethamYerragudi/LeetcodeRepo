# Problem 560: Subarray Sum Equals K
# Difficulty: Medium
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        seen = defaultdict(int)
        ans = 0
        for num in prefix_sum:
            complement = num - k
            if complement in seen:
                ans += seen[complement]
            seen[num] += 1
        return ans