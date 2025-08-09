# Problem 723: Candy Crush
# Difficulty: Medium
from collections import deque


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        U:
            I: a m x n matrix
            O: a m x n matrix which represents the stable grid
            C: N/A
            E: If the board is already stable -> return the board
        P:
            if no candies are crushed -> return board
            if no candies are dropped -> return board
            check all rows for multiple similar cells
            check all columns for multiple similar cells
            crush al same time (-1)
            drop:
                check column and if it has a negative 1, we shift all cells above down by the number of -1 cells in the column
        I:
        """

        def crush():
            crush = set()
            # rows
            for i in range(len(board) - 2):
                for j in range(len(board[i])):
                    if (
                        board[i][j] == board[i + 1][j]
                        and board[i + 1][j] == board[i + 2][j]
                        and board[i][j] != 0
                    ):
                        crush.add((i, j))
                        crush.add((i + 1, j))
                        crush.add((i + 2, j))

            for i in range(len(board)):
                for j in range(len(board[i]) - 2):
                    if (
                        board[i][j] == board[i][j + 1]
                        and board[i][j + 1] == board[i][j + 2]
                        and board[i][j] != 0
                    ):
                        crush.add((i, j))
                        crush.add((i, j + 1))
                        crush.add((i, j + 2))
            for cell in crush:
                x, y = cell
                board[x][y] = -1

            return len(crush) != 0

        def drop():
            dropped = False
            for j in range(len(board[0])):
                q = deque()
                for i in range(len(board) - 1, -1, -1):
                    if board[i][j] != -1:
                        q.append(board[i][j])
                if q:
                    dropped = True
                for i in range(len(board) - 1, -1, -1):
                    if q:
                        cell = q.popleft()
                        board[i][j] = cell
                    else:
                        board[i][j] = 0
            return dropped

        while True:
            crushed = crush()
            if not crushed:
                return board
            dropped = drop()
            if not dropped:
                return board
