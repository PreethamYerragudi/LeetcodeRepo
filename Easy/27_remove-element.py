# Problem 27: Remove Element
# Difficulty: Easy
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        ans = len(nums)
        while r >= 0 and nums[r] == val:
            r -= 1
            ans -= 1
        l = 0
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                ans -= 1
                l += 1
                r -= 1
                while nums[r] == val:
                    ans -= 1
                    r -= 1
            else:
                l += 1
        print(nums)
        return ans
        