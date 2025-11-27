# Problem 2149: Rearrange Array Elements by Sign
# Difficulty: Medium
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = deque()
        neg = deque()
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        ans = []
        pos_turn = True
        while pos or neg:
            if pos_turn:
                ans.append(pos.popleft())
            else:
                ans.append(neg.popleft())
            pos_turn = not pos_turn
        return ans