# Problem 20: Valid Parentheses
# Difficulty: Easy
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set(['(', '{', '['])
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0