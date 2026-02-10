# Problem 547: Number of Provinces
# Difficulty: Medium
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j]:
                    graph[i].append(j) 
        
        seen = set()
        ans = 0
        q = deque()
        for i in range(n):
            if i not in seen:
                ans += 1
                q.append(i)
                seen.add(i)
                while q:
                    node = q.popleft()
                    for nx in graph[node]:
                        if nx not in seen:
                            q.append(nx)
                            seen.add(nx)
        return ans
