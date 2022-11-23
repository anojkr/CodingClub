import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap = collections.defaultdict(list)
        for ele in strs:
            Count = [0]*26
            for e in list(ele):
                Count[ord(e)-ord('a')]+=1
            HashMap[tuple(Count)].append(ele)
        return HashMap.values()