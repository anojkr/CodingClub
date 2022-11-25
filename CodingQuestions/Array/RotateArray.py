class Solution:

    def transpose(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        for i in range(0, R):
            for j in range(i + 1, C):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def rotateMatrix(self, matrix):
        low = 0
        high = len(matrix[0]) - 1
        while low < high:
            for i in range(0, len(matrix)):
                matrix[i][low], matrix[i][high] = matrix[i][high], matrix[i][low]
            low += 1
            high -= 1
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.rotateMatrix(matrix)




