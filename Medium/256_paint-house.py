# Problem 256: Paint House
# Difficulty: Medium
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        0: red
        1: green
        2: blue
        """
        @lru_cache()
        def paint(i, c):
            if i >= len(costs):
                return 0
            
            val = float('inf')
            for j in range(3):
                if j == c:
                    continue
                val = min(val, paint(i + 1, j))
            return costs[i][c] + val 

        return min(paint(0, 0), paint(0, 1), paint(0, 2))