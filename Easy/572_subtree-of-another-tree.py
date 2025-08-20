# Problem 572: Subtree of Another Tree
# Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isSubroot = False
        def isSame(node_p, node_q):
            if not node_p and not node_q:
                return True
            elif not node_p and node_q:
                return False
            elif not node_q and node_p:
                return False
            if node_p.val != node_q.val:
                return False

            left = isSame(node_p.left, node_q.left)
            right = isSame(node_p.right, node_q.right)

            return left and right
        def traverse(root):
            nonlocal isSubroot
            if root.left:
                traverse(root.left)
            if isSame(root,subRoot):
                isSubroot = True
                return
            if root.right:
                traverse(root.right)
        traverse(root)
        return isSubroot