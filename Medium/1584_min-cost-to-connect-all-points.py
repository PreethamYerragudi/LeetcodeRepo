# Problem 1584: Min Cost to Connect All Points
# Difficulty: Medium
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        seen = set()
        graph = defaultdict(list)
        def calc_dist(x1, y1, x2, y2):
            return abs(x2 - x1) + abs(y2 - y1)
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = calc_dist(x1, y1, x2, y2)
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        heap.append([0, 0])
        ans = 0
        while len(seen) < len(points):
            dist, point = heappop(heap)
            if point in seen:
                continue
            ans += dist
            seen.add(point)
            for d, n in graph[point]:
                if n not in seen:
                    heappush(heap, [d, n])
        return ans