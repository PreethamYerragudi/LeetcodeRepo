# Problem 342: Power of Four
# Difficulty: Easy
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 1
        while i <= n:
            if i == n:
                return True
            i = i * 4
        return False