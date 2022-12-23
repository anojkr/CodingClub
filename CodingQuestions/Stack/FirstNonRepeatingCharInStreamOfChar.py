import collections


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        Q = collections.deque()
        result = []
        arr = A
        N = len(A)

        for i in range(0, N):
            while len(Q) > 0 and arr[Q[0]] == arr[i]:
                Q.popleft()
            Q.append(i)
            if len(Q) > 0:
                result.append(arr[Q[0]])
            else:
                result.append("#")
        return "".join(map(str, result))
