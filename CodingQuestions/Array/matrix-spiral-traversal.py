class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix) - 1, len(matrix[0]) - 1

        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        result = []
        while left <= right and up <= down:

            if left <= right and up <= down:
                for i in range(left, right + 1):
                    result.append(matrix[up][i])
                up += 1

            if left <= right and up <= down:
                for i in range(up, down + 1):
                    result.append(matrix[i][right])
                right -= 1

            if left <= right and up <= down:
                for i in range(right, left - 1, -1):
                    result.append(matrix[down][i])
                down -= 1

            if left <= right and up <= down:
                for i in range(down, up - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
