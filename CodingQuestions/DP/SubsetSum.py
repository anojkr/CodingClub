class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    T = {}

    def subsetSum(self, arr, targetSum, N):

        if targetSum == 0 and N == -1:
            return True

        if N < 0 or targetSum < 0:
            return False

        if self.T.get((targetSum, N)) is not None:
            return self.T.get((targetSum, N))

        if arr[N] <= targetSum:
            self.T[(targetSum, N)] = self.subsetSum(arr, targetSum - arr[N], N - 1) or self.subsetSum(arr, targetSum,
                                                                                                      N - 1)
            return self.T.get((targetSum, N))
        else:
            self.T[(targetSum, N)] = self.subsetSum(arr, targetSum, N - 1)
            return self.T.get((targetSum, N))

    def solve(self, A, B):
        self.T = {}
        return 1 if self.subsetSum(A, B, len(A) - 1) == True else 0


