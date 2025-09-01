# Problem 2537: Count the Number of Good Subarrays
# Difficulty: Medium
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = Counter()
        right = -1
        ans, n = 0, len(nums)
        same = 0
        for left in range(len(nums)):
            while same < k and right + 1 < n:
                right += 1
                same += count[nums[right]]
                count[nums[right]] += 1
            if same >= k:
                ans += n - right
            count[nums[left]] -= 1
            same -= count[nums[left]]
        return ans
            

            