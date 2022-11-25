class Solution:
    def climbStairs(self, n: int) -> int:

        Table = [0 for _ in range(n)]
        if n <= 2:
            return n
        Table[0] = 1
        Table[1] = 2
        for i in range(2, n):
            Table[i] = Table[i - 1] + Table[i - 2]
        return Table[n - 1]
