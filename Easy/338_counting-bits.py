# Problem 338: Counting Bits
# Difficulty: Easy
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            str = bin(i)[2:]
            ans.append(Counter(str).get('1', 0))
        return ans