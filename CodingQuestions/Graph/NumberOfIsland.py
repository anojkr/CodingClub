class Solution:

    def bfs(self, grid, srcX, srcY):
        Q = deque()
        vis = set()
        Q.append((srcX, srcY))
        vis.add((srcX, srcY))
        M = len(grid)
        N = len(grid[0])

        while Q:
            nodeX, nodeY = Q.popleft()
            grid[nodeX][nodeY] = -1
            x = [-1, 0, 1, 0]
            y = [0, 1, 0, -1]
            for i in range(4):
                newNodeX = nodeX + x[i]
                newNodeY = nodeY + y[i]
                if newNodeX >= 0 and newNodeX < M and newNodeY >= 0 and newNodeY < N:
                    if (newNodeX, newNodeY) not in vis and grid[newNodeX][newNodeY] == '1':
                        Q.append((newNodeX, newNodeY))
                        vis.add((newNodeX, newNodeY))

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count