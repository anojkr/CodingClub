# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        Q = collections.deque()
        if root == None:
            return 0
        Q.append((root, 0))
        while len(Q) > 0:
            node, currSum = Q.pop()
            if node:
                currSum += node.val
                if (currSum == targetSum) and node.left == None and node.right == None:
                    return True
                Q.append((node.left, currSum))
                Q.append((node.right, currSum))
        return False
