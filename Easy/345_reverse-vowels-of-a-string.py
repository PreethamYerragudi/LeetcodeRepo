# Problem 345: Reverse Vowels of a String
# Difficulty: Easy
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        vowels = set(['A', 'E', 'I', 'O', 'U'])
        while left < right:
            if s[left].upper() in vowels and s[right].upper() in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left].upper() in vowels:
                right -= 1
            elif s[right].upper() in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(s)
        