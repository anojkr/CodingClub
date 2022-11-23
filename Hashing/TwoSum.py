class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for i, ele in enumerate(nums):
            rem = target - ele
            if rem in HashMap:
                return [HashMap[rem], i]
            else:
                HashMap[ele] = i
