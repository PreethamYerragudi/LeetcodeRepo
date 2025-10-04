# Problem 875: Koko Eating Bananas
# Difficulty: Medium
class Solution:
    def check(self, pace):
        total = 0
        for num in self.piles:
            total += math.ceil(num / pace)
        return total <= self.h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.h = h
        self.piles = piles
        left, right = 1 , max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.check(mid):
                right = mid
            else:
                left = mid + 1
        return left
            