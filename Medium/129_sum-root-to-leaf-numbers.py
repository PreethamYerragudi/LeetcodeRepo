# Problem 129: Sum Root to Leaf Numbers
# Difficulty: Medium
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root, "")])
        while q:
            node, val = q.popleft()
            val += str(node.val)
            if not node.left and not node.right:
                ans += int(val)
            if node.left:
                q.append((node.left, val))
            if node.right:
                q.append((node.right, val))
        return ans
                