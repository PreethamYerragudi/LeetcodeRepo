# Problem 120: Triangle
# Difficulty: Medium
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache
        def minPath(i, j):
            if i >= len(triangle) or j >= len(triangle[-1]):
                return 0
            return triangle[i][j] + min(minPath(i + 1, j), minPath(i + 1, j + 1))
        return minPath(0,0)