class Solution:
    T = []
    def solve(self, nums, targetSum, N):
        if targetSum == 0:
            return True

        if N < 0 or targetSum < 0:
            return False

        if self.T[targetSum][N] != -1:
            return self.T[targetSum][N]

        if nums[N] <= targetSum:
            self.T[targetSum][N] = self.solve(nums, targetSum - nums[N], N - 1) or self.solve(nums, targetSum, N - 1)
            return self.T[targetSum][N]
        else:
            self.T[targetSum][N] = self.solve(nums, targetSum, N - 1)
            return self.T[targetSum][N]

    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        target = totalSum // 2 + 10
        self.T = [[-1 for _ in range(250)] for _ in range(target)]
        if totalSum % 2 != 0:
            return False
        else:
            return self.solve(nums, totalSum // 2, len(nums) - 1)
