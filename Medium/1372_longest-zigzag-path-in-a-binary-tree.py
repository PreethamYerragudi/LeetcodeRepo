# Problem 1372: Longest ZigZag Path in a Binary Tree
# Difficulty: Medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
            U:
                I: The root of a binary tree
                O: An integer
                C: N/A
                E: If there is only a root -> 0
            P:
                (node, edge, length)
                (1, True, 1)

                (2, False, prev_length + 1)
                (2, True, 1)
            I:
        """

        return max(dfs(root, True, 0),
        dfs(root, False, 0))

def dfs(curr_node, right, length):
    if not curr_node:
        return length - 1
    if right:
        return max(dfs(curr_node.left, False, length + 1), 
        dfs(curr_node.right, True, 1))
    else:
        return max(dfs(curr_node.left, False, 1),
        dfs(curr_node.right, True, length + 1))
