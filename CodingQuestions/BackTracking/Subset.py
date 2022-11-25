import copy

class Solution:
    def getSubset(self, nums, start, N, arr, result):
        if start == N:
            result.append(copy.deepcopy(arr))
            return
        self.getSubset(nums, start + 1, N, arr, result)
        arr.append(nums[start])
        self.getSubset(nums, start + 1, N, arr, result)
        arr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        result = []
        self.getSubset(nums, 0, len(nums), arr, result)
        return result
