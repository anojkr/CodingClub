import collections
def topView(root):
    #Write your code here
        Q = collections.deque()
        HashMap = collections.defaultdict(list)
        Q.append((root, 0, 0))
        while len(Q) > 0:
            node, keyVal, level = Q.popleft()
            if node:
                HashMap[keyVal].append((node.info, level))
                Q.append((node.left, keyVal - 1, level + 1))
                Q.append((node.right, keyVal + 1, level + 1))

        keys = sorted(HashMap.keys())
        result = []
        for key in keys:
            val = list(HashMap.get(key))
            resp = sorted(val, key=lambda x: (x[1], x[0]))
            result.append(resp[0][0])
        print(" ".join(map(str,result)))
        return result