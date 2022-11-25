# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symmetric(self, L, R):
        if L == None and  R == None:
            return True
        if L != None  and R!= None and L.val == R.val:
            return self.symmetric(L.right, R.left) and self.symmetric(L.left, R.right)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric(root, root)