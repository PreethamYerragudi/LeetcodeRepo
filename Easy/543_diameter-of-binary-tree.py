# Problem 543: Diameter of Binary Tree
# Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left + right + 2)
            return max(left, right) + 1
        if not root:
            return 0
        dfs(root)
        return diameter
