class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)
        DP = [[0 for j in range(N + 1)] for i in range(M + 1)]
        maxSubstring = 0
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    DP[i][j] = 1 + DP[i - 1][j - 1]
                    maxSubstring = max(maxSubstring, DP[i][j])
                else:
                    DP[i][j] = 0
        return maxSubstring
