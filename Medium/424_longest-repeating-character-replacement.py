# Problem 424: Longest Repeating Character Replacement
# Difficulty: Medium
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        count = defaultdict(int)
        def numDiff(count):
            arr = [v for k, v in count.items()]
            a = max(arr)
            s = sum(arr)
            return s - a
        for r in range(len(s)):
            count[s[r]] += 1
            while numDiff(count) > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
