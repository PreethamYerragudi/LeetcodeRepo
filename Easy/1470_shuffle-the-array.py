# Problem 1470: Shuffle the Array
# Difficulty: Easy
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums) // 2
        ans = [-1 for _ in range(2*n)]
        for i in range(n):
            ans[i*2] = nums[i]
            ans[i*2 + 1] = nums[n + i]
        return ans