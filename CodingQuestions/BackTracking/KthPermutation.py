import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings

    def getPermutation(self, A, B):
        n = A
        k = B
        res = ''
        i = 0
        new_k = k - 1
        nums = [str(i) for i in range(1, n + 1)]
        while i < n - 1:
            fact_nm1 = math.factorial(n - i - 1)
            o1 = (new_k // fact_nm1)
            new_k %= fact_nm1
            res += nums.pop(o1)
            i += 1
        res += nums[0]
        return res

