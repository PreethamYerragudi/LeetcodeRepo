# Problem 1046: Last Stone Weight
# Difficulty: Easy
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)
        while len(heap) > 1:
            y = -heappop(heap)
            x = -heappop(heap)
            if y != x:
                heappush(heap, -(y-x))
        if not heap:
            return 0
        return -heappop(heap)