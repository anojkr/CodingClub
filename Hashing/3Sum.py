class Solution:
    def twoSum(self, nums, i):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            A = nums[i]
            B = nums[l]
            C = nums[r]
            if (A + B + C == 0):
                return [A, B, C]
            elif A + B + C < 0:
                l += 1
            elif A + B + C > 0:
                r -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, ele in enumerate(nums):
            ans = self.twoSum(nums, i)
            if ans != None:
                res.append(ans)
        return res
