# Problem 1958: Check if Move is Legal
# Difficulty: Medium
class Solution:
    def checkMove(
        self, board: List[List[str]], rMove: int, cMove: int, color: str
    ) -> bool:
        """
        U:
            I: 2x2 grid
            O: a boolean
            C: N/A
            E: N/A
        P:

        I:
        """

        def isValid(cell):
            return (
                cell[0] >= 0
                and cell[0] < 8
                and cell[1] >= 0
                and cell[1] < 8
                and not board[cell[0]][cell[1]] == "."
            )

        dirs = [(1, 0), (-1, 0), (1, 1), (-1, -1), (0, 1), (0, -1), (1, -1), (-1, 1)]
        oppositeColor = "B" if color == "W" else "W"
        for dir in dirs:
            cell = (rMove, cMove)
            cell = (cell[0] + dir[0], cell[1] + dir[1])
            num_middle = 0
            while isValid(cell):
                if board[cell[0]][cell[1]] == oppositeColor:
                    num_middle += 1
                    cell = (cell[0] + dir[0], cell[1] + dir[1])
                elif board[cell[0]][cell[1]] == color:
                    if num_middle >= 1:
                        return True
                    break
        return False
