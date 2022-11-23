class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        arrOne = m - 1
        arrTwo = n - 1
        k = m + n - 1
        while arrTwo >= 0:
            if arrOne >= 0 and nums1[arrOne] >= nums2[arrTwo]:
                nums1[k] = nums1[arrOne]
                arrOne -= 1
                k -= 1
            else:
                nums1[k] = nums2[arrTwo]
                k -= 1
                arrTwo -= 1
