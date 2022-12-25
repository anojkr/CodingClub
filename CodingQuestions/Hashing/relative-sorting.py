from collections import defaultdict


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        HashMap = defaultdict(int)
        for ele in arr1:
            HashMap[ele] += 1

        response = []
        for ele in arr2:
            count = HashMap.get(ele)
            response.extend([ele] * count)
            HashMap.pop(ele)

        keys = sorted(HashMap.keys())
        for ele in keys:
            count = HashMap.get(ele)
            response.extend([ele] * count)
            HashMap.pop(ele)
        return response