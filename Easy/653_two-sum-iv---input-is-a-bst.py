# Problem 653: Two Sum IV - Input is a BST
# Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def traverse(root):
            if not root:
                return
            arr.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        seen = set()
        for num in arr:
            if k - num in seen:
                return True
            if num not in seen:
                seen.add(num)
        return False