# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q !=None:
            return False
        elif p != None and q == None:
            return False
        elif p == None and q == None:
            return True
        if p.val != q.val:
            return False
        else:
            L = self.isSameTree(p.left, q.left)
            R = self.isSameTree(p.right, q.right)
            return L and R