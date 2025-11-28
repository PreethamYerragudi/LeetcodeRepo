# Problem 78: Subsets
# Difficulty: Medium
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path, remaining):
            nonlocal ans
            ans.append(path[:])
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[i + 1:])
                path.pop()
        backtrack([], nums)
        return ans