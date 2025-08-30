# Problem 128: Longest Consecutive Sequence
# Difficulty: Medium
import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        heapq.heapify(nums)
        prev_num = None
        ans = 0
        temp = 0
        while nums:
            curr = heapq.heappop(nums)
            if prev_num != None:
                if curr - prev_num == 1:
                    temp += 1
                else:
                    ans = max(ans, temp)
                    temp = 1
            else:
                temp += 1
            prev_num = curr
        ans = max(ans, temp)
        return ans
                
