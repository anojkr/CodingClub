# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self, root):
        if root == None:
            return True, 0
        LB, LH = self.height(root.left)
        RB, RH = self.height(root.right)
        if LB == True and RB == True and abs(LH - RH) <= 1:
            return True, max(LH, RH) + 1
        else:
            return False, max(LH, RH) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.height(root)[0]
