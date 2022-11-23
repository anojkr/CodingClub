# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
import itertools


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        Q = collections.deque()
        Q.append(root)
        result = []
        while len(Q) > 0:
            size = len(Q)
            resp = []
            while size > 0:
                size -= 1
                node = Q.popleft()
                if node:
                    resp.append(node.val)
                    Q.append(node.left)
                    Q.append(node.right)
            if len(resp) > 0:
                result.append(resp)
        return result







