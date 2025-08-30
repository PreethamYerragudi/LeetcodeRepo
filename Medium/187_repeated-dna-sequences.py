# Problem 187: Repeated DNA Sequences
# Difficulty: Medium
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        seen = set()

        for i in range(0, len(s) - 10 + 1):
            if s[i : i + 10] in seen:
                ans.add(s[i : i + 10])
            else:
                seen.add(s[i : i + 10])
        
        return list(ans)