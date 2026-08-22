# Problem 1047: Remove All Adjacent Duplicates In String
# Difficulty: Easy
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        return "".join(stack)