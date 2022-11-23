# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        Q = collections.deque()
        HashMap = collections.defaultdict(list)
        Q.append((root, 0, 0))
        while len(Q) > 0:
            node, keyVal, level = Q.popleft()
            if node:
                HashMap[keyVal].append((node.val, level))
                Q.append((node.left, keyVal - 1, level + 1))
                Q.append((node.right, keyVal + 1, level + 1))

        keys = sorted(HashMap.keys())
        result = []
        for key in keys:
            val = list(HashMap.get(key))
            resp = sorted(val, key=lambda x: (x[1], x[0]))
            result.append([x[0] for x in resp])
        return result




