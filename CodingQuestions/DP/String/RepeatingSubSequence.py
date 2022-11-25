class Solution:
    # @param A : string
    # @return an integer
    T = {}

    def lcs(self, text1, text2, M, N):
        if M == 0 or N == 0:
            return 0

        if self.T.get((M, N)) != None:
            return self.T.get((M, N))
        if text1[M - 1] == text2[N - 1] and M - 1 != N - 1:
            self.T[(M, N)] = 1 + self.lcs(text1, text2, M - 1, N - 1)
            return self.T.get((M, N))
        else:
            self.T[(M, N)] = max(self.lcs(text1, text2, M, N - 1), self.lcs(text1, text2, M - 1, N))
            return self.T.get((M, N))

    def anytwo(self, A):
        self.T = {}
        ans = self.lcs(A, A, len(A), len(A))
        return 1 if ans >= 2 else 0
