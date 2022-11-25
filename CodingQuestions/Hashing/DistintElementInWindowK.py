import collections
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        HashMap = collections.defaultdict(int)
        for i in range(0, B):
            HashMap[A[i]] += 1

        result = []
        i = 0
        result.append(len(HashMap))
        for j in range(B, len(A)):
            ele = A[j]
            HashMap[A[j]] += 1
            if HashMap[A[i]] == 1:
                HashMap.pop(A[i])
            else:
                HashMap[A[i]] -= 1
            i += 1
            j += 1
            result.append(len(HashMap))
        return result

