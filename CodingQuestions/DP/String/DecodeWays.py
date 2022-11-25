class Solution:
    T = {}
    def solve(self, s, i, N):
        if i >= N:
            return 1
        patA = int(s[i])
        ways = 0
        if self.T.get(i) != None:
            return self.T.get(i)
        if int(patA) == 0:
            return 0
        if patA >= 1 and patA <= 9:
            ways = self.solve(s, i + 1, N)
        if i + 1 < N:
            patB = int(s[i] + s[i + 1])
            if patB >= 10 and patB <= 26:
                ways += self.solve(s, i + 2, N)
        self.T[i] = ways
        return self.T.get(i)

    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
            return 0
        self.T = {}
        return self.solve(s, 0, len(s))
