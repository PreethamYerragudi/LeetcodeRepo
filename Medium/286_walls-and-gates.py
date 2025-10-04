# Problem 286: Walls and Gates
# Difficulty: Medium
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dirs = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )

        q = deque()
        seen = set()
        def isValid(coord):
            x, y = coord
            return x >= 0 and y >= 0 and x < len(rooms) and y < len(rooms[0]) and rooms[x][y] != 0 and rooms[x][y] != -1 and coord not in seen
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    seen.clear()
                    q.append((i, j))
                dist = 0
                while q:
                    for _ in range(len(q)):
                        x, y = q.popleft()
                        rooms[x][y] = min(dist, rooms[x][y])
                        for a, b in dirs:
                            coord = x + a, y + b
                            if isValid(coord):
                                q.append(coord)
                                seen.add(coord)
                    dist += 1
                            
