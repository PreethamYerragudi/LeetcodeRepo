# Problem 2144: Minimum Cost of Buying Candies With Discount
# Difficulty: Easy
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost)
        ans = 0
        while cost:
            ans += cost.pop()
            if cost:
                ans += cost.pop()
            if cost:
                cost.pop()
        return ans
        