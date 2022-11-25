import collections
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        Q = collections.deque()
        res = []
        HashMap = {}
        for ele in A:
            if HashMap.get(ele) == None:
                HashMap[ele] = 1
                Q.append(ele)
            else:
                HashMap[ele] += 1
            while len(Q) > 0 and HashMap.get(Q[0]) > 1:
                Q.popleft()
            if len(Q) == 0:
                res.append("#")
            else:
                res.append(Q[0])
        return "".join(res)
