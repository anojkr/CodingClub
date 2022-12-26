import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        HashMap = {}
        i = 0
        j = 0
        maxRes = 0
        N = len(s)
        while i < N and j < N:
            ele = s[j]
            if ele in HashMap:
                while s[i] != ele:
                    HashMap.pop(s[i])
                    i+=1
                HashMap.pop(s[i])
                HashMap[ele]=True
                i+=1
                j+=1
            else:
                maxRes = max(maxRes, j-i+1)
                HashMap[ele]=True
                j+=1
        return maxRes
