# Problem 347: Top K Frequent Elements
# Difficulty: Medium
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        ans = sorted(dict.keys(), key=lambda key: dict.get(key), reverse=True)[0:k]
        return ans
