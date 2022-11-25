class Solution:
    # @param A : list of list of chars

    def dfs(self, grid, i, j):

        M = len(grid)
        N = len(grid[0])

        stack = []
        vis = set()
        stack.append((i, j))
        vis.add((i, j))

        while stack:
            nodeX, nodeY = stack.pop()
            grid[nodeX][nodeY] = "*"
            x = [-1, 0, 1, 0]
            y = [0, 1, 0, -1]
            for i in range(4):
                newX = nodeX + x[i]
                newY = nodeY + y[i]
                if newX >= 0 and newX < M and newY >= 0 and newY < N and grid[newX][newY] == "O":
                    if (newX, newY) not in vis:
                        vis.add((newX, newY))
                        stack.append((newX, newY))

    def solve(self, A):

        M = len(A)
        N = len(A[0])
        items = set()

        if M == 1 and N == 1:
            return

        for i in range(M):
            for j in range(N):
                if (i == 0 or i == M - 1) and A[i][j] == "O":
                    items.add((i, j))
                elif (j == 0 or j == N - 1) and A[i][j] == "O":
                    items.add((i, j))

        for item in items:
            x, y = item
            self.dfs(A, x, y)

        for i in range(M):
            for j in range(N):
                if A[i][j] == "*":
                    A[i][j] = "O"
                elif A[i][j] == "O":
                    A[i][j] = "X"






