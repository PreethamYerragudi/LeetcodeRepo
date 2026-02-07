# Problem 540: Single Element in a Sorted Array
# Difficulty: Medium
class Solution:
    """
    6 // 2
    112233
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l <= r:
            m = (l + r) // 2
            print("m: ",m)
            if m + 1 < len(nums) and nums[m + 1] == nums[m]:
                if (m - l) % 2 != 0:
                    r = m - 1
                else:
                    l = m + 2
            elif m - 1 >= 0 and nums[m - 1] == nums[m]:
                if (m - l - 1) % 2 != 0:
                    r = m - 2
                else:
                    l = m + 1
            else:
                return nums[m]
        return 0