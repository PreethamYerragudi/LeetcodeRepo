# Problem 42: Trapping Rain Water
# Difficulty: Hard
class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        right = [0] * len(height)
        max_left = height[0]
        max_right = height[-1]
        ans = 0
        for i in range(1, len(height)):
            left.append(max_left)
            max_left = max(max_left, height[i])
        for i in range(len(height) - 2, -1, -1):
            right[i + 1] = max_right
            max_right = max(max_right, height[i])
        for i in range(len(left)):
            water = min(left[i], right[i]) - height[i]
            if water > 0:
                ans += water
        return ans


