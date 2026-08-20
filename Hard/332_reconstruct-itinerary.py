# Problem 332: Reconstruct Itinerary
# Difficulty: Hard
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        seen = set()
        for i in range(len(tickets)):
            source, target = tickets[i]
            graph[source].append((target, i))
        for k in graph.keys():
            graph[k] = sorted(graph[k])
        ans = []
        def dfs(node, edge):
            seen.add(edge)
            for n, e in graph[node]:
                if e not in seen:
                    dfs(n, e)
            ans.append(node)
        dfs("JFK", -1)
        return ans[::-1]