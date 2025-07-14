from collections import deque


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        #BFS Approach

        queue = deque()
        queue.appendleft(root)
        while queue:
            node = queue.pop()
            if node.val == targetSum and not node.left and not node.right:
                return True
            if node.left:
                queue.appendleft(
                    TreeNode(node.val + node.left.val, node.left.left,
                             node.left.right))
            if node.right:
                queue.appendleft(
                    TreeNode(node.val + node.right.val, node.right.left,
                             node.right.right))
        return False
