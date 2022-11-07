def rotateArrayByOnePosition(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low += 1


rotateArrayByOnePosition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
