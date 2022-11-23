"""

"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        Stack = []
        HashMap = {}
        for i in range(len(nums2) - 1, -1, -1):
            ele = nums2[i]
            if len(Stack) == 0:
                Stack.append(ele)
            else:
                while len(Stack) > 0 and Stack[-1] < ele:
                    Stack.pop()
                if Stack:
                    HashMap[ele] = Stack[-1]
                Stack.append(ele)
        response = [-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            ele = nums1[i]
            nxtGE = HashMap.get(ele)
            response[i] = nxtGE if nxtGE != None else -1
        return response
