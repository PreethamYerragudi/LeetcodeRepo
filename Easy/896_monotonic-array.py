# Problem 896: Monotonic Array
# Difficulty: Easy
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        increasing = -1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            if nums[i - 1] > nums[i]:
                if increasing == -1:
                    increasing = 1
                elif not increasing:
                    return False
            else:
                if increasing == -1:
                    increasing = 0
                elif increasing:
                    return False
        return True
                