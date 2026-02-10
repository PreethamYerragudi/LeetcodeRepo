# Problem 240: Search a 2D Matrix II
# Difficulty: Medium
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l, r = 0, len(row) - 1
            while l <= r:
                m = (l + r) // 2
                if row[m] == target:
                    return True
                elif target < row[m]:
                    r = m - 1
                else:
                    l = m + 1
        return False
