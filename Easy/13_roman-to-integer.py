# Problem 13: Roman to Integer
# Difficulty: Easy
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        stack = []
        lst = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for char in s:
            if stack:
                if lst[char] > lst[stack[-1]]:
                    val = stack.pop()
                    ans += lst[char] - lst[val]
                else:
                    val = stack.pop()
                    ans += lst[val]
                    stack.append(char)
            else:
                stack.append(char)
        if stack:
            ans += lst[stack.pop()]
        return ans
