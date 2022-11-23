class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        HashMap = {}
        ans = 0
        for ele in nums:
            HashMap[ele] = True
        for ele in nums:
            numCount = ele
            if numCount - 1 not in HashMap:
                count = 0
                while numCount in HashMap:
                    numCount += 1
                    count += 1
                ans = max(ans, count)
        return ans
