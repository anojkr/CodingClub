class Solution:
    # @param A : list of integers
    # @return an integer

    T = []

    def solveMinSubsetSum(self, currSum, totalSum, N, nums):
        if N <= 0:
            # If we have reached last element. The difference of two sums
            # Sum of one subset is sumCalculated,
            # sum of other subset is sumTotal-sumCalculated.
            # Return absolute difference of two sums
            return abs((totalSum - currSum) - currSum)

        if self.T[currSum][N] != -1:
            return self.T[currSum][N]

        self.T[currSum][N] = min(
            self.solveMinSubsetSum(currSum, totalSum, N - 1, nums),
            self.solveMinSubsetSum(currSum + nums[N], totalSum, N - 1, nums)
        )
        return self.T[currSum][N]

    def solve(self, A):
        nums = A
        totalSum = sum(nums)
        self.T = [[-1 for _ in range(len(nums) + 10)] for _ in range(totalSum + 10)]
        return self.solveMinSubsetSum(0, totalSum, len(nums) - 1, nums)
