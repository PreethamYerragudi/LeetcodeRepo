# Problem 994: Rotting Oranges
# Difficulty: Medium
from collections import deque


class Solution:
    """
    U:
        I: m x n grid with values representing the status / existance of oranges in that space
        O: an integer that represents the minutes till no fresh orange remains
        C: N/A
        E:
            If there are no oranges -> 0
    P:
        algo orangesRotting (grid: m x n):
            q = queue
            seen = set
            min = 0
            for orange in grid:
                if orange is rotten:
                    add cell to queue
                    add cell to seen
            while q:
                for orange in current q:
                    for each valid 4-directionally adjacent new_cell:
                        if not seen new_cell and new_cell contains fresh orange:
                            new_cell = 2
                            seen.add(new_cell)
                            q.add(new_cell)
                min += 1
            return min
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(cell):
            return (
                cell[0] >= 0
                and cell[1] >= 0
                and cell[0] < len(grid)
                and cell[1] < len(grid[0])
                and cell not in seen
                and grid[cell[0]][cell[1]] == 1
            )

        q = deque()
        minutes = 0
        seen = set()
        empty = True
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    empty = False
                if grid[i][j] == 2:
                    empty = False
                    q.append((i, j))
                    seen.add((i, j))
        if empty:
            return 0
        while q:
            length = len(q)
            for _ in range(length):
                cell = q.popleft()
                for dir in dirs:
                    new_cell = (cell[0] + dir[0], cell[1] + dir[1])
                    if isValid(new_cell):
                        grid[new_cell[0]][new_cell[1]] = 2
                        q.append(new_cell)
                        seen.add(new_cell)
            minutes += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return minutes - 1
