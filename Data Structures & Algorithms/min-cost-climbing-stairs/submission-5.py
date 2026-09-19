class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        table = [0] * (len(cost) + 1)

        for i in range(2, len(cost)+1):        # Can look back at either i-1 or i-2 to start/ choose the minimum choice
            table[i] = min(table[i-1] + cost[i-1], table[i-2] + cost[i-2])
        
        return table[len(cost)]
        