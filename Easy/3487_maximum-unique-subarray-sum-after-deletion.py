# Problem 3487: Maximum Unique Subarray Sum After Deletion
# Difficulty: Easy


class Solution(object):

  def maxSum(self, nums):
    """
      :type nums: List[int]
      :rtype: int
      """
    ans = 0
    seen = set()
    for num in nums:
      if num > 0 and num not in seen:
        ans += num
        seen.add(num)
    return ans if ans > 0 else max(nums)
