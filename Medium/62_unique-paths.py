# Problem 62: Unique Paths
# Difficulty: Medium
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dest = (m - 1, n - 1)
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        def isValid(x, y):
            return x < m and y < n and x >= 0 and y >= 0
        def numPaths(x, y):
            if (x, y) == dest:
                return 1
            if memo[x][y] != -1:
                return memo[x][y]
            total = 0
            if isValid(x + 1,  y):
                total += numPaths(x + 1, y)
            if isValid(x,  y + 1):
                total += numPaths(x, y + 1)
            memo[x][y] = total
            return memo[x][y]
        return numPaths(0, 0)
