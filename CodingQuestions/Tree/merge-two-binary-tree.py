# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
sys.setrecursionlimit(10**5)
class Solution:

    def merge(self, p, q):
        if p == None and q == None:
            return p
        if p == None:
            return q
        elif q == None:
            return p
        p.val +=q.val
        p.left = self.merge(p.left, q.left)
        p.right= self.merge(p.right, q.right)
        return p

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.merge(root1, root2)