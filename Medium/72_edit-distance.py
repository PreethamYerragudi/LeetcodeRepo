# Problem 72: Edit Distance
# Difficulty: Medium
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache()
        def solve(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return solve(i + 1, j + 1)
            return 1 + min(solve(i + 1, j), solve(i, j + 1), solve(i + 1, j + 1))
        return solve(0,0)