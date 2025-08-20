# Problem 230: Kth Smallest Element in a BST
# Difficulty: Medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def traverse(root):
            nonlocal arr
            if root.left:
                traverse(root.left)
            arr.append(root.val)
            if root.right:
                traverse(root.right)
        traverse(root)
        return arr[k - 1]