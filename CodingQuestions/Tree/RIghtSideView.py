# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        Q = collections.deque()
        HashMap = collections.defaultdict(list)
        Q.append((root, 0))

        while len(Q) > 0:
            node, level = Q.pop()
            if node:
                HashMap[level].append(node.val)
                Q.append((node.right, level+1))
                Q.append((node.left, level + 1))
        result = []
        for key, value in  HashMap.items():
            result.append(value[-1])
        return result