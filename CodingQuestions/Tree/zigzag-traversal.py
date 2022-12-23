from collections import deque, defaultdict
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        Q = deque()
        Q.append(root)
        result = []
        flag = False
        while Q:
            size = len(Q)
            resp = []
            while size:
                node = Q.popleft()
                if node:
                    resp.append(node.val)
                    Q.append(node.left)
                    Q.append(node.right)
                size-=1
            if flag:
                resp.reverse()
            if len(resp) > 0:
                result.append(resp)
            flag = not flag
        return result
