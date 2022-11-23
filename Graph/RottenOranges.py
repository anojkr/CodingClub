import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Q = collections.deque()
        vis = set()
        M = len(grid)
        N = len(grid[0])

        freshCount = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    vis.add((i, j))
                    Q.append((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1

        if freshCount == 0:
            return 0

        ans = 0
        while Q:
            T = len(Q)
            ans += 1
            while T > 0:
                T -= 1
                nodeX, nodeY = Q.popleft()
                x = [-1, 0, 1, 0]
                y = [0, 1, 0, -1]
                for i in range(4):
                    newX = nodeX + x[i]
                    newY = nodeY + y[i]
                    if newX >= 0 and newX < M and newY >= 0 and newY < N and grid[newX][newY] == 1:
                        if (newX, newY) not in vis:
                            vis.add((newX, newY))
                            Q.append((newX, newY))
                            grid[newX][newY] = 2

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return -1
        return ans - 1

