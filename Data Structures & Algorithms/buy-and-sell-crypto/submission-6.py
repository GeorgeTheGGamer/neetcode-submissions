class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Single day to buy
        # Different day in future to sell
        # Maximum profit -> Sliding window
        # O(n) answer

        maxProfit = 0
        minBuy = prices[0]

        for r in range(len(prices)):
            minBuy = min(minBuy,prices[r])      # Left pointer is the minimum so far
            maxProfit = max(maxProfit, prices[r] - minBuy)
        return maxProfit     
                
