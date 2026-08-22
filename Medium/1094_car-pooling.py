# Problem 1094: Car Pooling
# Difficulty: Medium
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for n, s, e in trips:
            heapq.heappush(heap, (s, 1, n))
            heapq.heappush(heap, (e, 0, n))
        num_picked = 0
        while heap:
            loc, pick, num = heapq.heappop(heap)
            if not pick:
                num_picked -= num
            else:
                num_picked += num
                if num_picked > capacity:
                    return False
        return True