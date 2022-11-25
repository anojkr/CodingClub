class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        u, d = 0, len(matrix) - 1
        res = []
        step = 0
        while l <= r and u <= d:
            match (step % 4):
                case 0:
                    for i in range(l, r+1):
                        res.append(matrix[u][i])
                    u += 1
                case 1:
                    for i in range(u, d+1):
                        res.append(matrix[i][r])
                    r -= 1
                case 2:
                    for i in range(r, l-1, -1):
                        res.append(matrix[d][i])
                    d -= 1
                case 3:
                    for i in range(d, u-1, -1):
                        res.append(matrix[i][l])
                    l += 1
            step += 1
        return res