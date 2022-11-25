import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        HashMap = collections.defaultdict(int)
        for ele in t:
            HashMap[ele] += 1
        count = 0
        i = 0
        j = 0
        N = len(s)
        while i < N and j < N:
            if s[j] in HashMap:
                count += 1
            while count == len(t):
                i = j + 1
                count = 0
            j += 1
            print(i, j, count)
