# Problem 1209: Remove All Adjacent Duplicates in String II
# Difficulty: Medium
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                v = (char, stack[-1][1] + 1)
            else:
                v = (char, 1)
            if v[1] >= k:
                for _ in range(k - 1):
                    stack.pop()
            else:
                stack.append(v)
        ans = ""
        for c, i in stack:
            ans += c
        return ans