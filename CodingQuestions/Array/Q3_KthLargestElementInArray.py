import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            Time Complexity: O(K + (N-K) * Log K)
            Auxiliary Space: O(K)
        """
        heapQ = nums[0:k]
        heapq.heapify(heapQ)
        for i in range(k, len(nums)):
            ele = nums[i]
            if heapQ[0] <= ele:
                heapq.heappop(heapQ)
                heapq.heappush(heapQ, ele)
        return heapQ[0]
