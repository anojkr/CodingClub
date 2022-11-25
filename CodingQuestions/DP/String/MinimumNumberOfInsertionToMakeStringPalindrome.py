class Solution:
    T = {}

    def solve(self, text1, text2, M, N):
        if M < 0 or N < 0:
            return 0

        if self.T.get((M, N)) != None:
            return self.T.get((M, N))

        if text1[M] == text2[N]:
            self.T[(M, N)] = 1 + self.solve(text1, text2, M - 1, N - 1)
            return self.T.get((M, N))
        else:
            self.T[(M, N)] = max(self.solve(text1, text2, M, N - 1), self.solve(text1, text2, M - 1, N))
            return self.T.get((M, N))

    def minInsertions(self, s: str) -> int:
        self.T = {}
        text1 = s
        text2 = "".join(reversed(s))
        return len(s) - self.solve(text1, text2, len(text1) - 1, len(text2) - 1)