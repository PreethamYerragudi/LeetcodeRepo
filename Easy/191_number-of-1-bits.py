# Problem 191: Number of 1 Bits
# Difficulty: Easy
class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(bin(n)[2:])['1']