class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxGlobal = nums[0]
        maxCurrent = nums[0]
        current = 0
        for i in range(0, len(nums)):
            current = current + nums[i]
            maxCurrent = max(maxCurrent, current)
            maxGlobal = max(maxGlobal, maxCurrent)
            if current < 0:
                current = 0
        return maxGlobal
