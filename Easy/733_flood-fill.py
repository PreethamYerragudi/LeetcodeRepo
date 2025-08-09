# Problem 733: Flood Fill
# Difficulty: Easy
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        seen = set()
        def isValid(coord):
            x, y = coord
            return x >= 0 and x < len(image) and y >= 0 and y < len(image[0]) and coord not in seen and image[x][y] == starting_color
        q = deque([(sr, sc)])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            curr = q.popleft()
            image[curr[0]][curr[1]] = color
            seen.add(curr)
            for dir in dirs:
                x, y = dir
                new = (curr[0] + x, curr[1] + y)
                if isValid(new):
                    q.append(new)
        return image