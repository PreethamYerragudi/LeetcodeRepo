# Problem 118: Pascal's Triangle
# Difficulty: Easy
import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            curr_level = []
            for j in range(i+1):
                curr_level.append(comb(i, j))
            ans.append(curr_level)
        return ans 