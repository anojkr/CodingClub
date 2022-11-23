import  collections
class Solution:
    def frequencySort(self, s: str) -> str:
        HashMap = collections.defaultdict(int)
        for index,ele in enumerate(s):
            HashMap[ele]+=1
        resp = sorted(HashMap.items(), key = lambda x : x[1], reverse = True)
        result = [ele*fre for ele,fre in resp]
        return "".join(map(str, result))