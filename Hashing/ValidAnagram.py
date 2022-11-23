class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HashOne = [0]*26
        HashTwo = [0]*26
        for ele in s:
            char = ord(ele)-ord('a')
            HashOne[char]+=1
        for ele in t:
            char = ord(ele)-ord('a')
            HashTwo[char]+=1
        return HashOne == HashTwo