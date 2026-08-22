# Problem 3536: Maximum Product of Two Digits
# Difficulty: Easy
class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        while n:
            arr.append(n % 10)
            n //= 10
        arr.sort()
        return arr[-1] * arr[-2]