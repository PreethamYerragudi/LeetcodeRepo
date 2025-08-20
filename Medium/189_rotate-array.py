# Problem 189: Rotate Array
# Difficulty: Medium
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = len(nums) - (k % len(nums) if k > len(nums) else k)
        print(shift)
        for _ in range(shift):
            nums.append(nums.pop(0))