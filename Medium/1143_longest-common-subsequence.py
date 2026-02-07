# Problem 1143: Longest Common Subsequence
# Difficulty: Medium
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def longest_common_subsequence(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] != text2[j]:
                dp[i][j] = max(longest_common_subsequence(i, j + 1), longest_common_subsequence(i + 1, j))
            else:
                dp[i][j] = 1 + longest_common_subsequence(i + 1, j + 1)
            return dp[i][j]
        
        return longest_common_subsequence(0, 0)
        
