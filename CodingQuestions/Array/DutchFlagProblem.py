class Solution:
    def sortColors(self, nums: List[int]) -> None:
        mid = 0
        low = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
