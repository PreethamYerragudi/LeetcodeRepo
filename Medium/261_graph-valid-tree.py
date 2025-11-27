# Problem 261: Graph Valid Tree
# Difficulty: Medium
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        cycle_detected = False
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        def dfs(parent, curr):
            nonlocal cycle_detected
            seen.add(curr)
            for n in graph[curr]:
                if n == parent:
                    continue
                print(curr, n)
                if n in seen:
                    cycle_detected = True
                    return
                dfs(curr, n)
        dfs(None, 0)
        if cycle_detected:
            return False
        return len(seen) == n
                