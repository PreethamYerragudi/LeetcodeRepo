# Problem 215: Kth Largest Element in an Array
# Difficulty: Medium
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums] 
        heapify(heap)
        for _ in range(k - 1):
            heappop(heap)
        return -heappop(heap)