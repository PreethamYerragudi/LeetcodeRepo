# Problem 125: Valid Palindrome
# Difficulty: Easy
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = "".join(c for c in s if c.isalnum())
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left] == s[right]:
                return False
            left += 1
            right -= 1
        return True