# Problem 100: Same Tree
# Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
            U:
                I: Two root nodes for two binary trees
                O: A boolean
                C: N/A
                E: If both nodes are empty -> true
                    If one node is empty but the other isn't -> false
            P:
        """
        def traversal(node_p, node_q):
            if not node_p and not node_q:
                return True
            elif not node_p and node_q:
                return False
            elif not node_q and node_p:
                return False
            if node_p.val != node_q.val:
                return False

            left = traversal(node_p.left, node_q.left)
            right = traversal(node_p.right, node_q.right)

            return left and right
            
        return traversal(p, q)
