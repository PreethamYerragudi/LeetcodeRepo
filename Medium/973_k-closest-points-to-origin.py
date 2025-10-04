# Problem 973: K Closest Points to Origin
# Difficulty: Medium
import heapq
class Solution:
    def calcDist(self, x, y):
        return sqrt(x**2 + y**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x, y = points[i]
            dist = self.calcDist(x, y)
            heappush(heap, (dist, i))
        ans = []
        for _ in range(k):
            ans.append(points[heappop(heap)[1]])
        return ans