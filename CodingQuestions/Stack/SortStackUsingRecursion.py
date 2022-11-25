
import sys
sys.setrecursionlimit(1500)

class Solution:
    # @param A : list of integers
    # @return a list of integers
    
    def insert(self, A, ele):
        if len(A) == 0  or A[-1] <= ele:
            A.append(ele)
        else:
            item = A.pop()
            self.insert(A, ele)
            A.append(item)

    def solve(self, A):
        if len(A) > 0:
            ele = A.pop()
            self.solve(A)
            self.insert(A, ele)
        return A