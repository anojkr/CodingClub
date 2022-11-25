class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        for r in range(1, len(A)):
            for c in range(len(A[0])):
                if A[r][c] == 1:
                    A[r][c] += A[r - 1][c]
        best_ans = 0
        for hist in A:
            ans = self.solve_hist(hist)
            best_ans = max(ans, best_ans)
        return best_ans

    def solve_hist(self, hist):
        hist.append(0)
        stack = [(-1, -1)]
        best_ans = 0
        for r_op, val in enumerate(hist):
            while stack[-1][0] > val:
                v, i = stack.pop()
                l_op = stack[-1][1]
                l_cl = l_op + 1
                ans = v * (r_op - l_cl)
                best_ans = max(ans, best_ans)
            stack.append((val, r_op))
        return best_ans



