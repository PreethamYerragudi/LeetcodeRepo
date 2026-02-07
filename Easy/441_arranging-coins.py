# Problem 441: Arranging Coins
# Difficulty: Easy
class Solution:
    def arrangeCoins(self, n: int) -> int:
        def sum_to_n_formula(n):
            if n < 1:
                return 0
            # Use // for integer division if an integer result is strictly required
            # otherwise, standard division returns a float
            return (n * (n + 1)) // 2
        l, r = 0, n
        while l <= r:
            m = (l + r) // 2
            if sum_to_n_formula(m) > n:
                r = m - 1
            else:
                l = m + 1
        return r