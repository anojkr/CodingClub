class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer

    def dfs(self, grid, i, j, word, vis, result):

        M = len(grid) - 1
        N = len(grid[0]) - 1

        currString = "".join(map(str, result))
        if len(result) == len(word) and currString == word:
            return True

        if i < 0 and i > M and j < 0 and j > N:
            return False

        vis.add((i, j))
        result.append(grid[i][j])

        x = [-1, 0, 1, 0]
        y = [0, 1, 0, -1]
        ans = False
        for k in range(4):
            newX = i + x[k]
            newY = j + y[k]
            if newX >= 0 and newX <= M and newY >= 0 and newY <= N:
                if (newX, newY) not in vis:
                    ans = ans or self.dfs(grid, newX, newY, word, vis, result)
        vis.remove((i, j))
        result.pop()
        return ans

    def exist(self, A, B):
        grid = [list(_) for _ in A]
        M = len(grid)
        N = len(grid[0])
        for i in range(0, M):
            for j in range(0, N):
                if grid[i][j] == B[0]:
                    vis = set()
                    result = []
                    ans = self.dfs(grid, i, j, B, vis, result)
                    if ans == True:
                        return 1

        return 0
