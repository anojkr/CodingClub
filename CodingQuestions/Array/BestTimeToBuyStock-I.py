class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buyPrice = prices[0]
        N = len(prices)
        profit = 0
        for i in range(1, N):
            if buyPrice >= prices[i]:
                buyPrice = prices[i]
            profit = max(profit, prices[i]-buyPrice)
        return profit




import collections
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        T = [-1]*len(prices)

        N = len(prices)
        j = len(prices)-1
        Q = collections.deque()
        while j >= 0:
            while len(Q)>0 and Q[0] < prices[j]:
                Q.pop()
            if Q:
                T[j] = Q[0]
            Q.append(prices[j])
            j-=1
        ans = 0
        for i in range(N):
            if T[i]!=-1:
                ans = max(ans, abs(T[i]-prices[i]))
        return ans



