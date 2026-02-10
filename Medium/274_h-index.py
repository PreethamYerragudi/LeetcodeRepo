# Problem 274: H-Index
# Difficulty: Medium
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(arr, h):
            return (sum([int(arr[i] >= h) for i in range(len(arr))]) >= h)
        l, r = 0, len(citations)
        ans = 0
        while l <= r:
            h = (l + r) // 2
            if check(citations, h):
                ans = h
                l = h + 1
            else:
                r = h - 1
        return ans
        
                