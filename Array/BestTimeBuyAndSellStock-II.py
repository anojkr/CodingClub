"""
Algorithm
1. Initialize maxProfit = 0. Initially consider the first stock value as both the peak and valley for a new transaction.
2. Linearly iterate over the prices[] array starting from day 2 or index = 1 to the end of the array.
3. Check if the current stock price is greater than the previous stock price. If it is true, then the current stock price will be the peak.
    a.If the last price is the peak stock price, then maxProfit = maxProfit + (peak - valley).
4. If the current stock price is not greater than the previous, then maxProfit = maxProfit + (peak - valley). The new transaction should start from the ith day. The valley will be prices[i]    and the new peak will be the valley.
5. Return the maxProfit.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Analysis the peak and valley  pattern in array
        """
        N = len(prices)
        peak = prices[0]
        profit = 0
        vally = prices[0]
        for i in range(0, N):
            if peak <= prices[i]:
                peak = prices[i]
            elif peak > prices[i]:
                profit += peak - vally
                peak = prices[i]
                vally = prices[i]
        profit += peak - vally
        return profit

