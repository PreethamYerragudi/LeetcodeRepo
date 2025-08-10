# Problem 231: Power of Two
# Difficulty: Easy
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x <= n:
            if x == n:
                return True
            x = x * 2
        return False