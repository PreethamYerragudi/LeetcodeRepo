# Problem 207: Course Schedule
# Difficulty: Medium
import heapq
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        seen = set()
        ind = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            graph[i] = []
        for i, j in prerequisites:
            graph[j].append(i)
            ind[i] += 1
        q = deque()
        while len(seen) < numCourses:
            for i, val in enumerate(ind):
                if val == 0 and i not in seen:
                    q.append(i)
                    seen.add(i)
            if not q:
                return False
            while q:
                node = q.popleft()
                for n in graph[node]:
                    ind[n] -= 1
        return True
        