class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic window to find maximum profit
        profit = 0          # This will track the profit
        minBuy = prices[0]
        
        for r in range(len(prices)):
            minBuy = min(minBuy, prices[r])
            current = prices[r] - minBuy     # Must be calcualted each time 
            profit = max(current, profit)

        return profit
                
