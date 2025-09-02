# Problem 992: Subarrays with K Different Integers
# Difficulty: Hard
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
            1, 2, 1, 2, 3
        """
        def sliding_window(k):
            count = defaultdict(int)
            left = 0
            ans = 0
            for right in range(len(nums)):
                count[nums[right]] += 1
                distinct = len(count)
                while distinct > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                        distinct -= 1
                    left += 1
                ans += (right - left) + 1
            return ans
        return sliding_window(k) - sliding_window(k-1)

        
    
