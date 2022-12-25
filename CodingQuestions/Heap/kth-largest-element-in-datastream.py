import heapq as hq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.size = k
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        if len(self.heap) < self.size:
            hq.heappush(self.heap, val)
            return self.heap[0]
        else:
            while len(self.heap) > self.size:
                hq.heappop(self.heap)
            if self.heap[0] <= val:
                hq.heappop(self.heap)
                hq.heappush(self.heap, val)
            return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)