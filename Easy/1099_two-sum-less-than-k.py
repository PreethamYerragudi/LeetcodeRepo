# Problem 1099: Two Sum Less Than K
# Difficulty: Easy
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        seen = []
        maxVal = -1
        for num in nums:
            for number in seen:
                if number + num < k:
                    maxVal = max(maxVal, number + num)
            seen.append(num)
        return maxVal