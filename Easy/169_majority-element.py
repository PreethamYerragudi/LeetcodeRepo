# Problem 169: Majority Element
# Difficulty: Easy
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = sorted(Counter(nums).items(), key=lambda x : x[1], reverse=True)
        return dic[0][0]
