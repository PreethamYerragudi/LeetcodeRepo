# Problem 112: Path Sum
# Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        print(root)
        def dfs(node, sum, target):
            if sum == target and not node.left and not node.right:
                return True
            left = False
            right = False
            if node.left:
                left = dfs(node.left, sum + node.left.val, target)
            if node.right:
                right = dfs(node.right, sum + node.right.val, target)
            return left or right
        if not root:
            return False
        return dfs(root, root.val, targetSum)