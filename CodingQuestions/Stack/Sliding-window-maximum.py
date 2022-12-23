from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        Q = deque()
        res = []
        for i in range(0, N):
            while Q and Q[0] < i-k+1:
                Q.popleft()
            while Q and nums[Q[-1]] <= nums[i]:
                Q.pop()
            Q.append(i)
            if Q:
                res.append(nums[Q[0]])
        return res[k-1:]