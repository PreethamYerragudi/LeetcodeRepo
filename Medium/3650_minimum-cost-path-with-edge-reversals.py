# Problem 3650: Minimum Cost Path with Edge Reversals
# Difficulty: Medium
import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for x, y, w in edges:
            graph[x].append((y, w))
            graph[y].append((x, 2 * w))

        heap = [[0,0]]
        seen = set()
        while heap:
            w, node = heappop(heap)
            if node == n - 1:
                return w
            elif node in seen:
                continue
            seen.add(node)
            for neighbor, c in graph[node]:
                if neighbor in seen:
                    continue
                heappush(heap, [w + c, neighbor])
        return -1

