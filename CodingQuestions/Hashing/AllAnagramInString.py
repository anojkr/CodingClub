class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pHashMap = [0] * 26
        HashMap = {}
        for ele in p:
            item = ord(ele) - ord('a')
            pHashMap[item] += 1
        HashMap[tuple(pHashMap)] = True

        sHashMap = [0] * 26
        M = len(p)
        N = len(s)
        i = 0
        j = 0
        res = []
        while i < N and j < N:
            iItem = ord(s[i]) - ord('a')
            jItem = ord(s[j]) - ord('a')
            if j < M:
                sHashMap[jItem] += 1
                j += 1
            else:
                sHashMap[iItem] -= 1
                sHashMap[jItem] += 1
                j += 1
                i += 1
            if tuple(sHashMap) in HashMap:
                res.append(i)
        return res
