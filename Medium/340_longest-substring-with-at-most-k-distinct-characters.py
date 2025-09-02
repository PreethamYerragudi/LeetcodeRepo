# Problem 340: Longest Substring with At Most K Distinct Characters
# Difficulty: Medium
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(s)):
            count[s[right]] += 1
            distinct = len(count)
            while distinct > k:
                count[s[left]] -= 1
                if count[s[left]] <= 0:
                    del count[s[left]]
                    distinct -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans