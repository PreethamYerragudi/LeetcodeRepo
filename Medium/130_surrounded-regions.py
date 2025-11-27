# Problem 130: Surrounded Regions
# Difficulty: Medium
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen = set()

        def onEdge(x, y):
            return x == len(board) - 1 or y == len(board[0]) - 1 or x == 0 or y == 0

        def isValid(x, y):
            return (
                x < len(board)
                and y < len(board[0])
                and x >= 0
                and y >= 0
                and (x, y) not in seen
                and board[x][y] == "O"
            )

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if isValid(i, j):
                    q = deque([(i, j)])
                    seen.add((i, j))
                    edge = False
                    region = []
                    while q:
                        x, y = q.popleft()
                        region.append((x, y))
                        if onEdge(x, y):
                            edge = True
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if isValid(nx, ny):
                                q.append((nx, ny))
                                seen.add((nx, ny))
                    if not edge:
                        for x, y in region:
                            board[x][y] = "X"
