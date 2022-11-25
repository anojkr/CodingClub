# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if  root == None:
            return 0
        if root.left == None and root.right==None:
            return 1
        L = self.maxDepth(root.left)
        R = self.maxDepth(root.right)
        if root.left  == None:
            return R+1
        if root.right == None:
            return L+1
        return max(L,R)+1