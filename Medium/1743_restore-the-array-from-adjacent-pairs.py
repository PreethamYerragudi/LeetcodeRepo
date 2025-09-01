# Problem 1743: Restore the Array From Adjacent Pairs
# Difficulty: Medium
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)

        for a, b in adjacentPairs:
            dic[a].append(b)
            dic[b].append(a)
        
        ans = []

        def dfs(num, prev):
            ans.append(num)
            for child in dic[num]:
                if child != prev:
                    dfs(child, num)
        for num, value in dic.items():
            if len(value) == 1:
                dfs(num, -1)
                return ans




