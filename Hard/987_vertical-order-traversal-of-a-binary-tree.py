# Problem 987: Vertical Order Traversal of a Binary Tree
# Difficulty: Hard
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        q = deque([(0, root)])
        while q:
            l = len(q)
            temp = defaultdict(list)
            for _ in range(l):
                v, n = q.popleft()
                temp[v].append(n.val)
                if n.right:
                    q.append((v + 1, n.right))
                if n.left:
                    q.append((v - 1, n.left))
            for k, v in temp.items():
                v.sort()
                for i in v:
                    ans[k].append(i)
        arr = [v for k, v in sorted(ans.items(), key= lambda x : x[0])]
        return arr