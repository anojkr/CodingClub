# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dia = 0

    def getDiameter(self, root):
        if root == None: return 0
        L = self.getDiameter(root.left)
        R = self.getDiameter(root.right)
        if L + R > self.dia:
            self.dia = L + R
        return max(L, R) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.getDiameter(root)
        return self.dia


