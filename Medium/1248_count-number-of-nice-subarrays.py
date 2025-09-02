# Problem 1248: Count Number of Nice Subarrays
# Difficulty: Medium
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        new_nums = [(num % 2) for num in nums]
        total = 0
        dic = defaultdict(int)
        dic[0] += 1
        ans = 0
        for num in new_nums:
            total += num
            complement = total - k
            if complement in dic:
                ans += dic[complement]
            dic[total] += 1
        
        return ans
        
        
    