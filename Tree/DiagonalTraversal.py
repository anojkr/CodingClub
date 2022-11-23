# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import collections
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):

        Q = collections.deque()
        HashMap = collections.defaultdict(list)
        Q.append((A, 0))

        while len(Q) > 0:
            node, pos = Q.pop()
            if node:
                HashMap[pos].append(node.val)
                Q.append((node.right, pos))
                Q.append((node.left, pos + 1))

        result = []
        keys = sorted(list(HashMap.keys()))
        for key in keys:
            result = result + list(HashMap.get(key))
        return result
