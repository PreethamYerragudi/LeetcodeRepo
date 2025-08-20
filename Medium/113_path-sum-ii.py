# Problem 113: Path Sum II
# Difficulty: Medium
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque([(root, [])])
        while q:
            node, lst = q.popleft()
            lst.append(node.val)
            if not node.right and not node.left:
                if sum(lst) == targetSum:
                    ans.append(lst)
            if node.left:
                q.append((node.left, lst[:]))
            if node.right:
                q.append((node.right, lst[:]))
        return ans
