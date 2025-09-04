# Problem 84: Largest Rectangle in Histogram
# Difficulty: Hard
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1, -1)]
        ans = 0
        for i in range(len(heights)):
            curr_height, curr_idx = heights[i], i
            while stack[-1][0] > curr_height:
                check_height, check_i = stack.pop()
                ans = max(ans, check_height * (curr_idx - stack[-1][1] - 1))
            stack.append((curr_height, curr_idx))
        print(stack)
        while len(stack) > 1:
            check_height, check_i = stack.pop()
            ans = max(ans, check_height * (len(heights) - stack[-1][1] - 1))
        return ans
