# Problem 279: Perfect Squares
# Difficulty: Medium
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        seen = set()
        nums = []
        i = 1
        while i**2 <= n:
            nums.append(i**2)
            i += 1
        level = 0
        que = deque()
        que.append(0)
        seen.add(0)
        while que:
            length = len(que)
            for _ in range(length):
                total = que.popleft()
                if total == n:
                    return level
                for num in nums:
                    if not total + num in seen and not total + num > n:
                        que.append(total + num)
                        seen.add(total + num)
            level += 1
        return -1