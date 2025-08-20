# Problem 200: Number of Islands
# Difficulty: Medium
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        q = deque()
        seen = [[0] * len(grid[0]) for _ in range(len(grid))]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isValid(i, j):
            return (
                i >= 0
                and j >= 0
                and i < len(grid)
                and j < len(grid[0])
                and grid[i][j] == '1'
                and not seen[i][j]
            )

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not seen[i][j]:
                    q.append((i, j))
                    seen[i][j] = 1
                    while q:
                        x, y = q.popleft()
                        for dir in dirs:
                            new_i = x + dir[0]
                            new_j = y + dir[1]
                            if isValid(new_i, new_j):
                                q.append((new_i, new_j))
                                seen[new_i][new_j] = 1
                    ans += 1
        return ans
