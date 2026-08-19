# Problem 97: Interleaving String
# Difficulty: Medium
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @lru_cache()
        def solve(i, j, k):
            if i == len(s1) or j == len(s2):
                if i != len(s1):
                    return s3[k:] == s1[i:]
                elif j != len(s2):
                    return s3[k:] == s2[j:]
                return True
            val = False
            if s1[i] == s3[k]:
                val |= solve(i + 1, j, k + 1)
            if s2[j] == s3[k]:
                val |= solve(i, j + 1, k + 1)
            return val
        return solve(0,0,0)