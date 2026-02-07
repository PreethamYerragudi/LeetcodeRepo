# Problem 236: Lowest Common Ancestor of a Binary Tree
# Difficulty: Medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = 0
        def findNode(root, p, q):
            nonlocal ans
            if not root:
                return False
            if not root.left and not root.right:
                return root == p or root == q
            v = findNode(root.left, p, q) + findNode(root.right, p, q) + (root == p or root == q)
            if v >= 2:
                ans = root
                return False
            return v
        findNode(root, p, q)
        return ans