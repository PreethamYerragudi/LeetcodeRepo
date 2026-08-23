# Problem 486: Predict the Winner
# Difficulty: Medium
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def solve(i, j):
            if i == j:
                return nums[i]
            return max(
                nums[i] - solve(i + 1, j),
                nums[j] - solve(i, j - 1)
            )
        return solve(0, len(nums) - 1) >= 0