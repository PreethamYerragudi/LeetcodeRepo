# Problem 151: Reverse Words in a String
# Difficulty: Medium
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        return " ".join(arr[::-1])