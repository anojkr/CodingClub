import sys
import collections

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])

        Q = collections.deque()
        Q.append((0,0, grid[0][0]))
        vis = set()
        ans = sys.maxsize
        while Q:
            nodeX, nodeY, pathSum = Q.popleft()
            vis.add((nodeX, nodeY))
            if nodeX == M-1  and nodeY == N-1:
                ans = min(ans, pathSum)
            x = [0,1]
            y = [1,0]
            for i in range(2):
                newX = nodeX + x[i]
                newY = nodeY + y[i]
                if newX >= 0 and newX < M and newY >=0  and newY <N:
                    if (newX, newY) not in vis:
                        Q.append((newX, newY, pathSum+grid[newX][newY]))
        return ans