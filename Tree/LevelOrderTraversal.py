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
        Q.append((root, 0))
        resp = []
        while len(Q) > 0:
            node, level = Q.popleft()
            if node:
                resp.append((level, node.val))
                Q.append((node.left, level + 1))
                Q.append((node.right, level + 1))

        r = itertools.groupby(resp, key=lambda x: x[0])
        result = []
        for key, group in r:
            result.append([x[1] for x in group])
        return result






