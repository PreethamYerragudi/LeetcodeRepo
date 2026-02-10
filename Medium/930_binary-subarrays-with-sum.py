# Problem 930: Binary Subarrays With Sum
# Difficulty: Medium
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def slide(goal):
            l = 0
            ans = 0
            count = 0
            for r in range(len(nums)):
                if nums[r] == 1:
                    count += 1
                while l <= r and count > goal:
                    if nums[l] == 1:
                        count -= 1
                    l += 1
                ans += r - l + 1
            return ans
        return slide(goal) - slide(goal - 1)
