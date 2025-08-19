# Problem 210: Course Schedule II
# Difficulty: Medium
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        q = deque()
        graph = {}
        for num in range(numCourses):
            graph[num] = []
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        graph = sorted(graph.items(), key = lambda x : len(x[1]))

        for item in graph:
            if len(item[1]) > 0:
                break
            q.append(item[0])
            graph.remove(item)
        while q:
            node = q.popleft()
            ans.append(node)
            i = 0
            while i < len(graph):
                item = graph[i]
                if node in item[1]:
                    item[1].remove(node)
                if len(item[1]) <= 0:
                    q.append(item[0])
                    graph.remove(item)
                else:
                    i += 1
        if not graph:
            return ans
        return []
        