# Problem 159: Longest Substring with At Most Two Distinct Characters
# Difficulty: Medium


class Solution(object):

  def lengthOfLongestSubstringTwoDistinct(self, s):
    """
      :type s: str
      :rtype: int
      """
    j = 0
    max_length = 0
    lst = {}
    for i in range(len(s)):
      lst[s[i]] = lst.get(s[i], 0) + 1
      while len(lst) > 2:
        lst[s[j]] -= 1
        if lst[s[j]] == 0:
          lst.pop(s[j])
        j += 1
      max_length = max(max_length, i - j + 1)
    return max_length
