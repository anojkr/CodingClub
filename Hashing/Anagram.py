class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        HashMapOne = [0] * len(p)
        HashMap = {}
        for index, ele in enumerate(p):
            HashMap[ele] += 1
        HashMap[tuple(HashMapOne)] = True

        HashMapTwo = [0] * len(s)
        M = len(p)
        N = len(s)
        i = 0
        j = 0
        res = []
        while i < N and j < N:
            if j < M:
                HashMapTwo[s[j]] += 1
                j += 1
            else:
                HashMapTwo[s[i]] -= 1
                HashMapTwo[s[j]] += 1
                i += 1
                i -= 1
            if tuple(HashMapTwo) in HashMap:
                res.append(i)
        return res
