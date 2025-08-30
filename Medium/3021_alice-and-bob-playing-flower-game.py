# Problem 3021: Alice and Bob Playing Flower Game
# Difficulty: Medium
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        num_odd = m // 2 + (1 if m % 2 != 0 else 0)
        num_even = m - num_odd
        for i in range(1, n + 1):
            if i % 2 == 0:
                ans += num_odd
            else:
                ans += num_even
            
        return ans