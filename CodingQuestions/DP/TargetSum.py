class Solution:
    T = {}

    def solveTargetSum(self, currSum, targetSum, startIndex, nums, totalSum):
        if startIndex == len(nums):
            if currSum == targetSum:
                return 1
            else:
                return 0

        if startIndex > len(nums) - 1:
            return 0

        if self.T.get((currSum, startIndex)) != None:
            return self.T[(currSum, startIndex)]
        A = self.solveTargetSum(currSum + nums[startIndex], targetSum, startIndex + 1, nums, totalSum)
        B = self.solveTargetSum(currSum - nums[startIndex], targetSum, startIndex + 1, nums, totalSum)
        self.T[(currSum, startIndex)] = A + B
        return A + B

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        self.T = {}
        return self.solveTargetSum(0, target, 0, nums, totalSum)
