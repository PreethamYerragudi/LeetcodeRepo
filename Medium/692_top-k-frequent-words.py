# Problem 692: Top K Frequent Words
# Difficulty: Medium
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words).items()
        heap = [(-v, k) for k,v in freq]
        heapify(heap)
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
        return ans

        