# Problem 658: Find K Closest Elements
# Difficulty: Medium
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        nums = []
        for num in arr:
            nums.append((abs(num - x),num))
        heapq.heapify(nums)
        ans = []
        for i in range(k):
            print(i)
            ans.append(heapq.heappop(nums)[1])
        ans.sort()
        return ans
