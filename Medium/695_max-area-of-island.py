# Problem 695: Max Area of Island
# Difficulty: Medium
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        q = deque()
        dirs = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )
        seen = set()
        
        def isValid(x, y):
            return (
                x >= 0
                and y >=0
                and x < len(grid)
                and y < len(grid[0])
                and grid[x][y] == 1
                and (x, y) not in seen
            )
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = 0
                if isValid(i, j):
                    q.append((i, j))
                    seen.add((i, j))
                while q:
                    area += 1
                    x, y = q.popleft()
                    for a, b in dirs:
                        coord = (x + a, y + b)
                        if isValid(coord[0], coord[1]):
                            q.append(coord)
                            seen.add(coord)
                ans = max(ans, area)
        return ans
