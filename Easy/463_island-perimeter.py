# Problem 463: Island Perimeter
# Difficulty: Easy
from collections import deque


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        U:
            I: 2D Grid
            O: An Integer
            C: N/A
            E: If there is only one land cell -> 4
        P:

        I:
        """
        q = deque()
        perimeter = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        for row in range(len(grid)):
            if len(q) > 0:
                break
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    q.append((row, col))
                    seen.add((row, col))
                    break
        while q:
            square = q.popleft()
            for dir in dirs:
                x, y = dir
                new_square = (square[0] + x, square[1] + y)
                if (
                    new_square[0] < 0
                    or new_square[0] >= len(grid)
                    or new_square[1] < 0
                    or new_square[1] >= len(grid[0])
                ):
                    perimeter += 1
                elif not grid[new_square[0]][new_square[1]]:
                    perimeter += 1
                elif new_square not in seen:
                    q.append(new_square)
                    seen.add(new_square)
        return perimeter