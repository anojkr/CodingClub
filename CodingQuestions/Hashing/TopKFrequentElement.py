import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashMap = collections.defaultdict(int)
        for index, ele in enumerate(nums):
            HashMap[ele] += 1
        resp = sorted(HashMap.items(), key=lambda x: x[1], reverse=True)
        result = [ele for ele, fre in resp]
        return result[0:k]
