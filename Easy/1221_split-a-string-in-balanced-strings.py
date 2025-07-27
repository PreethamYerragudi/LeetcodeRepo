# Problem 1221: Split a String in Balanced Strings
# Difficulty: Easy
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        max = 0
        for char in s:
            if char == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                max += 1
        return max