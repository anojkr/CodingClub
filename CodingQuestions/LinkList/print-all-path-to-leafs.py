# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def traverse(self, root, stack, response):
        if root == None:
            return root
        stack.append(root.val)
        if root.left == None and root.right == None:
            response.append("->".join(map(str, stack)))
        self.traverse(root.left, stack, response)
        self.traverse(root.right, stack, response)
        stack.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        response = []
        self.traverse(root, [], response)
        return response

