# Problem 1944: Number of Visible People in a Queue
# Difficulty: Hard
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0 for _ in range(len(heights))]
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and stack[-1] <= heights[i]:
                stack.pop()
                ans[i] += 1
            if stack:
                ans[i] += 1
            stack.append(heights[i])
        return ans
            