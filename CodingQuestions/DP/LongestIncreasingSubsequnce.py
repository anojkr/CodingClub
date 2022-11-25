class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [1 for _ in range(len(nums))]
        LIS  = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and DP[i] < DP[j]+1:
                    DP[i] = 1 + DP[j]
                    LIS = max(LIS, 1 + DP[j])
        return LIS