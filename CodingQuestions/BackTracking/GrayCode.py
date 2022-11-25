import copy
class Solution:
    # @param A : integer
    # @return a list of integers

    def solve(self, i, A, arr, result):
        if i == A - 1:
            result.append(copy.deepcopy(arr))
            return
        newArr = []
        for j in arr:
            c = "0" + j
            newArr.append(c)
        arr.reverse()
        for j in arr:
            c = "1" + j
            newArr.append(c)
        self.solve(i + 1, A, newArr, result)

    def grayCode(self, A):
        arr = ["0", "1"]
        result = []
        self.solve(0, A, arr, result)
        resp = []
        for ele in result[0]:
            intArr = int(ele, 2)
            resp.append(intArr)
        return resp
