# Problem 36: Valid Sudoku
# Difficulty: Medium
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            check = set()
            for val in row:
                if val != '.' and val in check:
                    return False
                check.add(val)
        for j in range(len(board[0])):
            check = set()
            for i in range(len(board)):
                val = board[i][j]
                if val != '.' and val in check:
                    return False
                check.add(val)
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                check = set()
                for k in range(3):
                    for l in range(3):
                        val = board[i + k][j + l]
                        if val != '.' and val in check:
                            return False
                        check.add(val)

        return True
        