class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        StackOne = []
        StackTwo = []

        for ele in A:
            if len(StackOne) == 0 or  StackOne[-1] <= ele:
                StackOne.append(ele)
            else:
                while len(StackOne) > 0 and  StackOne[-1] > ele:
                    eleItem = StackOne.pop()
                    StackTwo.append(eleItem)
                StackOne.append(ele)
                while len(StackTwo) > 0:
                    StackOne.append(StackTwo.pop())
        return StackOne

