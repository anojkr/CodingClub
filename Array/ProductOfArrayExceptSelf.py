class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        preProd = [1 for _ in range(N)]
        sufProd = [1 for _ in range(N)]

        for i in range(1, N):
            preProd[i] = preProd[i - 1] * nums[i - 1]
        for i in range(N - 2, -1, -1):
            sufProd[i] = sufProd[i + 1] * nums[i + 1]

        res = []
        for i in range(0, N):
            res.append(preProd[i] * sufProd[i])
        return res
