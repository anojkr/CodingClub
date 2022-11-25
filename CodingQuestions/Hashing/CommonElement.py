class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        HashMap = {}
        numsSet = set()
        for ele in nums1:
            if ele not in HashMap:
                HashMap[ele] = True
        for ele in nums2:
            if ele in HashMap:
                numsSet.add(ele)
        return numsSet
