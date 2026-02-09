# Problem 796: Rotate String
# Difficulty: Easy
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i, c in enumerate(s):
            if c == goal[0]:
                if s[i:] + s[0:i] == goal:
                    return True
        return False