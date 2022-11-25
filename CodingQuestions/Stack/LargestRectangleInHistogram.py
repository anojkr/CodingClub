class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        N = len(heights)
        leftArr = [-1 for _ in range(N)]
        rightArr = [N for _ in range(N)]

        lStack = []
        for i in range(N):
            ele = heights[i]
            while len(lStack) > 0 and heights[lStack[-1]] > ele:
                lStack.pop()
            if len(lStack) > 0:
                leftArr[i] = lStack[-1]
            lStack.append(i)

        rStack = []
        for j in range(N - 1, -1, -1):
            ele = heights[j]
            while len(rStack) > 0 and heights[rStack[-1]] >= ele:
                rStack.pop()
            if len(rStack) > 0:
                rightArr[j] = rStack[-1]
            rStack.append(j)

        res = 0
        for i in range(N):
            ans = abs(leftArr[i] - rightArr[i]) - 1
            res = max(res, ans * heights[i])
        return res
