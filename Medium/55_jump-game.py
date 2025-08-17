# Problem 55: Jump Game
# Difficulty: Medium
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1] * len(nums)
        memo[-1] = True

        def jump(i):
            if memo[i] != -1:
                return memo[i]
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if jump(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return jump(0)
