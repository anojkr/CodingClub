class Solution:

    def solve(self, amount, N, nums, T):

        if amount == 0:
            return 1

        if N < 0 or amount < 0:
            return 0

        if T.get((amount, N)) != None:
            return T.get((amount, N))

        if amount >= nums[N]:
            T[(amount, N)] = self.solve(amount-nums[N], N, nums, T) +  self.solve(amount, N-1, nums, T)
            return T.get((amount, N))

        else:
            T[(amount, N)] = self.solve(amount, N-1, nums, T)
            return T.get((amount, N))


    def change(self, amount: int, coins: List[int]) -> int:
        T = {}
        return self.solve(amount, len(coins)-1, coins, T)