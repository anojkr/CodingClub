class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        Stack = []
        result = []
        for ele in A:
            while len(Stack) > 0 and Stack[-1] >= ele:
                Stack.pop()
            if len(Stack) > 0:
                result.append(Stack[-1])
            else:
                result.append(-1)
            Stack.append(ele)
        return result
