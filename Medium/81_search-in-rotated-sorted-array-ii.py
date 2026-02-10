# Problem 81: Search in Rotated Sorted Array II
# Difficulty: Medium
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True
        return False