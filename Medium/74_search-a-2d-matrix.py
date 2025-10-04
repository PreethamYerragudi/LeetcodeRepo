# Problem 74: Search a 2D Matrix
# Difficulty: Medium
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n

        while left < right:
            mid = left + (right - left) // 2
            i, j = mid // n, mid % n
            print(i, j)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid
            else:
                left = mid + 1
        return False