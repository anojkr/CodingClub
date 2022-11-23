class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left = [0 for _ in range(N)]
        right = [0 for _ in range(N)]
        lStack = []
        for i in range(N):
            hgt = height[i]
            if len(lStack) == 0 or lStack[-1] < hgt:
                left[i] = hgt
                lStack.append(hgt)
            else:
                left[i] = lStack[-1]

        rStack = []
        for i in range(N - 1, -1, -1):
            hgt = height[i]
            if len(rStack) == 0 or rStack[-1] < hgt:
                right[i] = hgt
                rStack.append(hgt)
            else:
                right[i] = rStack[-1]

        res = 0
        for i in range(N):
            res += min(left[i], right[i]) - height[i]
        return res
