# Problem 746: Min Cost Climbing Stairs
# Difficulty: Easy
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache
        def climb(step):
            if step >= len(cost):
                return 0
            return cost[step] + min(climb(step + 1), climb(step + 2))
        return min(climb(0), climb(1))
