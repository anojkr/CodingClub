"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        Q = collections.deque()
        Q.append(root)

        while len(Q) > 0:
            size = len(Q)
            while size > 0:
                size -= 1
                node = Q.popleft()
                if node:
                    if size > 0:
                        node.next = Q[0]
                    if node.left:
                        Q.append(node.left)
                    if node.right:
                        Q.append(node.right)
        return root
