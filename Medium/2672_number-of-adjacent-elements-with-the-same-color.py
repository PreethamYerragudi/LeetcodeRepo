# Problem 2672: Number of Adjacent Elements With the Same Color
# Difficulty: Medium
from collections import Counter
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [-1] * n
        ans = []
        for query in queries:
            curr = 0 if not ans else ans[-1]
            i, color = query[0], query[1]
            if colors[i] != -1:
                if i - 1 >= 0:
                    if colors[i - 1] == colors[i]:
                        curr -= 1
                if i + 1 < n:
                    if colors[i + 1] == colors[i]:
                        curr -= 1
            colors[i] = color
            if i - 1 >= 0:
                if colors[i - 1] == colors[i]:
                    curr += 1
            if i + 1 < n:
                if colors[i + 1] == colors[i]:
                    curr += 1
            ans.append(curr)
        return ans
                    
                    