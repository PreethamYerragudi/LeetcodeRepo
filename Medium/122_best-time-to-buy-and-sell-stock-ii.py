# Problem 122: Best Time to Buy and Sell Stock II
# Difficulty: Medium
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def solve(i, holding):
            if i >= len(prices):
                return 0
            if not holding:
                return max(
                    -prices[i] + solve(i + 1, 1), 
                    solve(i + 1, 0)
                    )
            else:
                return max(
                    prices[i] + solve(i, 0),
                    solve(i + 1, 1)
                )
        return solve(0, 0)