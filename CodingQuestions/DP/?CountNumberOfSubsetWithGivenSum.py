class Solution:
    T = []
    def solve(self, nums, targetSum, N):
        if targetSum == 0:
            return 1

        if N < 0 or targetSum < 0:
            return 0

        if self.T[targetSum][N] != -1:
            return self.T[targetSum][N]

        self.T[targetSum][N] = self.solve(nums, targetSum - nums[N], N - 1) +  self.solve(nums, targetSum, N -1)
        return self.T[targetSum][N]

    def numSubseq(self, nums: List[int], target: int) -> int:
        self.T = [[-1 for _ in range(len(nums)+10)] for _ in range(target+10)]
        return self.solve(nums, target, len(nums) - 1)