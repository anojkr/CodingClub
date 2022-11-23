import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        HashMap = collections.defaultdict(int)
        i = 0
        j = 0
        N = len(s)
        res = 0
        while i < N and j < N:
            ele = s[j]
            if ele in HashMap:
                HashMap[ele] += 1
                while HashMap[ele] > 1:
                    if HashMap[s[i]] == 1:
                        HashMap.pop(s[i])
                    else:
                        HashMap[s[i]] -= 1
                    i += 1
                j += 1
            else:
                HashMap[ele] += 1
                res = max(res, j - i + 1)
                j += 1
        return res
