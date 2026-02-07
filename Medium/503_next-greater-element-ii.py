# Problem 503: Next Greater Element II
# Difficulty: Medium
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1 for i in range(len(nums))]
        for _ in range(2):
            for i in range(len(nums) - 1, -1, -1):
                v = nums[i]
                while stack and stack[-1][0] <= v:
                    stack.pop()
                if stack:
                    res[i] = stack[-1][0]
                else:
                    res[i] = -1
                stack.append((v, i))
        return res