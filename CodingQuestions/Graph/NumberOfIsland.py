import collections
class Solution:

    def dfs(self, grid, i, j):

        M = len(grid)
        N = len(grid[0])

        vis = set()
        vis.add((i, j))

        Q = collections.deque()
        Q.append((i, j))
        vis.add((i, j))

        while Q:
            nodeX, nodeY = Q.pop()
            grid[nodeX][nodeY] = -1
            x = [-1, 0, 1, 0]
            y = [0, 1, 0, -1]

            for i in range(4):
                newX = nodeX + x[i]
                newY = nodeY + y[i]
                if newX >= 0 and newX < M and newY >= 0 and newY < N and grid[newX][newY] == "1":
                    if (newX, newY) not in vis:
                        vis.add((newX, newY))
                        Q.append((newX, newY))
                        vis.remove((newX, newY))

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count
