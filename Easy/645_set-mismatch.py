# Problem 645: Set Mismatch
# Difficulty: Easy
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        seen = set(nums)
        ans = []
        for k, v in count.items():
            if v == 2:
                ans.append(k)
        
        for i in range(len(nums)):
            if i + 1 not in seen:
                ans.append(i+1)
                return ans
                