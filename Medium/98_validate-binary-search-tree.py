# Problem 98: Validate Binary Search Tree
# Difficulty: Medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, upper, lower):
            if root.val >= upper or root.val <= lower:
                return False
            left = True
            right = True
            if root.left:
                left = validate(root.left, root.val, lower)
            if root.right:
                right = validate(root.right, upper, root.val)
            return left and right
        return validate(root, float('inf'), float('-inf'))
        
