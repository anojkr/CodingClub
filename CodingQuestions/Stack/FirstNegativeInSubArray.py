import collections


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        Q = collections.deque()
        result = []
        arr = A
        N = len(A)
        for i in range(0, N):
            if arr[i] < 0:
                Q.append(i)
            while len(Q) > 0 and i - Q[0] >= B:
                Q.popleft()
            if len(Q) > 0:
                result.append(arr[Q[0]])
            else:
                result.append(0)
        return result[B - 1:]
