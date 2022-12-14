class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        if nums[0] <= nums[-1]:
            return nums[0]

        while low < high:
            mid = low + (high - low) // 2
            if nums[low] < nums[mid]:
                low = mid
            else:
                high = mid

        return nums[low + 1]
