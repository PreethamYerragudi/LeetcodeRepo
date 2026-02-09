# Problem 2965: Find Missing and Repeated Values
# Difficulty: Easy
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        for row in grid:
            for n in row:
                count[n] += 1
        ans =[0, 0]
        for i in range(1, len(grid) ** len(grid) + 1):
            if count[i] == 0:
                ans[1] = i
                if ans[0] and ans[1]:
                    break
            if count[i] == 2:
                ans[0] = i
                if ans[0] and ans[1]:
                    break
        return ans