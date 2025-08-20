# Problem 226: Invert Binary Tree
# Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left and not root.right:
            return root
        def traverse(root):
            root.left, root.right = root.right, root.left
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(root)
        return root
        