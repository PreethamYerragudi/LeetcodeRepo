# Problem 102: Binary Tree Level Order Traversal
# Difficulty: Medium
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        ans = []
        while que:
            length = len(que)
            lst = []
            for _ in range(length):
                node = que.popleft()
                lst.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(lst)
        return ans
