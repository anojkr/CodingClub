import sys

sys.setrecursionlimit(10000)


class Solution:
    # @param A : string
    # @return an integer
    T = {}

    def lcs(self, text1, text2, M, N):
        if M == 0 or N == 0:
            return 0
        if self.T.get((M, N)) != None:
            return self.T.get((M, N))
        if text1[M - 1] == text2[N - 1]:
            self.T[(M, N)] = 1 + self.lcs(text1, text2, M - 1, N - 1)
            return self.T.get((M, N))
        else:
            subProbA = self.T.get((M, N - 1))
            subProbB = self.T.get((M - 1, N))
            A = subProbA if subProbA != None else self.lcs(text1, text2, M, N - 1)
            B = subProbB if subProbB != None else self.lcs(text1, text2, M - 1, N)
            self.T[(M, N)] = max(A, B)
            return self.T.get((M, N))

    def solve(self, A):
        self.T = {}
        B = "".join(reversed(A))
        return self.lcs(A, B, len(A), len(B))
