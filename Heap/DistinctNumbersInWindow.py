class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        N = len(A)
        HashMap = {}
        for i in range(B):
            if A[i] in HashMap:
                HashMap[A[i]] += 1
            else:
                HashMap[A[i]] = 1
        i = 0
        j = B
        res = []

        while i < N and j < N:
            res.append(len(HashMap))
            if A[j] not in HashMap:
                HashMap[A[j]] = 1
            else:
                HashMap[A[j]] += 1

            if HashMap[A[i]] > 1:
                HashMap[A[i]] -= 1
            else:
                HashMap.pop(A[i])
            i += 1
            j += 1
        res.append(len(HashMap))
        return res
