# Problem 3731: Find Missing Elements
# Difficulty: Easy
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m = max(nums)
        s = min(nums)
        seen = set(nums)
        ans = []
        for num in range(s, m + 1):
            if num not in seen:
                ans.append(num)
        return ans
            
