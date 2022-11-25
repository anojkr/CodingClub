import copy
class Solution:
    def permute(self, nums, start, N, result):
        if start == N:
            result.append(copy.deepcopy(nums))
            return
        else:
            s = set()
            for j in range(start, N + 1):
                if nums[j] not in s:
                    s.add(nums[j])
                    nums[start], nums[j] = nums[j], nums[start]
                    self.permute(nums, start + 1, N, result)
                    nums[start], nums[j] = nums[j], nums[start]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute(nums, 0, len(nums) - 1, result)
        return result
