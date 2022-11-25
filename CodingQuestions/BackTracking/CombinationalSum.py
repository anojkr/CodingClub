import copy


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    result = []
    def solve(self, arr, target, currArr, currSum, index, N, flag):

        if currSum > target:
            return None

        elif currSum == target:
            self.result.append(copy.deepcopy(currArr))
            return

        if index >= N:
            return

        else:
            if flag == False and arr[index - 1] == arr[index]:
                self.solve(arr, target, currArr, currSum, index + 1, N, False)

            else:
                self.solve(arr, target, currArr, currSum, index + 1, N, False)
                currArr.append(arr[index])
                self.solve(arr, target, currArr, currSum + arr[index], index + 1, N, True)
                currArr.pop()

    def combinationSum(self, A, B):
        self.result = []
        N = len(A)
        currArr = []
        A.sort()
        self.solve(A, B, currArr, 0, 0, N, True)
        return self.result
