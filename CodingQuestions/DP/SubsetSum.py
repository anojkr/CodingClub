class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def subsetSum(self, index, target, nums, T):

        if index <= 0 and target == 0:
            return True

        if index <= 0:
            return False

        if (index, target) in T:
            return T[(index, target)]

        if target >= nums[index - 1]:
            A = self.subsetSum(index - 1, target - nums[index - 1], nums, T)
            B = self.subsetSum(index - 1, target, nums, T)
            T[(index, target)] = A or B
            return T[(index, target)]
        else:
            T[(index, target)] = self.subsetSum(index - 1, target, nums, T)
            return T[(index, target)]

    def solve(self, A, B):
        T = {}
        return 1 if self.subsetSum(len(A), B, A, T) == True else 0
