import collections
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        HashMapArr1 = collections.defaultdict(int)
        HashMapArr2 = collections.defaultdict(int)
        for ele in arr1:
            HashMapArr1[ele] += 1
        for ele in arr2:
            HashMapArr2[ele] += 1

        resArr1 = []
        for ele in arr2:
            count = HashMapArr1[ele]
            while count > 0:
                resArr1.append(ele)
                count -= 1
        resArr2 = []
        for ele in arr1:
            if ele not in HashMapArr2:
                resArr2.append(ele)
        resArr2.sort()
        return resArr1 + resArr2
