import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        HashMap = collections.defaultdict(int)
        for index, ele in enumerate(s):
            HashMap[ele] += 1
        for index, ele in enumerate(s):
            if HashMap[ele] == 1:
                return index
        return -1