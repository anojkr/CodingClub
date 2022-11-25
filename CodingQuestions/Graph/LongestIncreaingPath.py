import  collections
class Solution:

    def dfs(self, grid, i, j):

        M = len(grid)
        N = len(grid[0])

        Q = collections.deque()
        Q.append((i, j, 1))

        vis = set()
        vis.add((i, j))
        ans = 0
        while Q:
            nodeX, nodeY, pathCount = Q.pop()
            ans = max(ans, pathCount)
            x = [-1, 0, 1, 0]
            y = [0, 1, 0, -1]
            for i in range(4):
                newX = nodeX + x[i]
                newY = nodeY + y[i]
                if newX >= 0 and newX < M and newY >= 0 and newY < N and grid[nodeX][nodeY] < grid[newX][newY]:
                    if (newX, newY) not in vis:
                        vis.add((newX, newY))
                        Q.append((newX, newY, pathCount + 1))
                        vis.remove((newX, newY))
        return ans

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        if M == 1 and N == 1:
            return 1
        response = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                response = max(response, self.dfs(matrix, i, j))
        return response
