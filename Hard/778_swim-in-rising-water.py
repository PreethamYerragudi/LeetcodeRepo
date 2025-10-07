# Problem 778: Swim in Rising Water
# Difficulty: Hard
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0], 0, 0]]
        dest = (len(grid) - 1, len(grid[0]) - 1)
        seen = set()
        dirs = (
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        )

        def isValid(x, y):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and (x, y) not in seen

        while minHeap:
            dist, i, j = heapq.heappop(minHeap)
            if (i, j) == dest:
                return dist
            if (i, j) in seen:
                continue
            seen.add((i, j))
            for x, y in dirs:
                new_x, new_y = i + x, j + y
                if isValid(new_x, new_y):
                    heapq.heappush(minHeap, [max(dist, grid[new_x][new_y]), new_x, new_y])
        return -1
                
