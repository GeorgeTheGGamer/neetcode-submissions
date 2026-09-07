class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic window to find maximum profit
        profit = 0          # This will track the profit
        # Both start from the left and dynamically increase               

        for r in range(len(prices)):
            l = 0
            while l != r:
                current = prices[r] - prices[l]
                profit = max(current, profit)
                l +=1
        
        return profit
                
