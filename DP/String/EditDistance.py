import sys

sys.setrecursionlimit(10000)


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    T = {}

    def editDistance(self, text1, text2, M, N):
        if M == 0:
            return N

        if N == 0:
            return M

        if self.T.get((M, N)) != None:
            return self.T.get((M, N))

        if text1[M - 1] == text2[N - 1]:
            self.T[(M, N)] = self.editDistance(text1, text2, M - 1, N - 1)
            return self.T.get((M, N))
        else:
            self.T[(M, N)] = 1 + min(self.editDistance(text1, text2, M, N - 1),
                                     self.editDistance(text1, text2, M - 1, N),
                                     self.editDistance(text1, text2, M - 1, N - 1))
            return self.T.get((M, N))

    def minDistance(self, A, B):
        self.T = {}
        return self.editDistance(A, B, len(A), len(B))
