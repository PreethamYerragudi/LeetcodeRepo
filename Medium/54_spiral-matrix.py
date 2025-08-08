# Problem 54: Spiral Matrix
# Difficulty: Medium
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        dir = 0
        seen = set()
        coord = (0, 0)
        seen.add(coord)
        ans = [matrix[0][0]]

        def isValid(coord):
            x, y = coord
            return (
                coord not in seen
                and x >= 0
                and x < len(matrix)
                and y >= 0
                and y < len(matrix[0])
            )

        while len(seen) < len(matrix) * len(matrix[0]):
            y, x = dirs[dir]
            new_coord = (coord[0] + x, coord[1] + y)
            if isValid(new_coord):
                seen.add(new_coord)
                coord = new_coord
                ans.append(matrix[coord[0]][coord[1]])
            else:
                dir = 0 if dir == 3 else dir + 1
        return ans
