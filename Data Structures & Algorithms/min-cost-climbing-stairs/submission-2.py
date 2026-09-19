class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Output is dynamic programming for minimum optimisation
        # Dynamic Programming for minimum cost
        
        top = len(cost)         # Top of stair index
        hashmap = {}
        def f(index):
            # Once we know we can reach the top of the stair case
            if index in hashmap:
                return hashmap[index]
            if (index+1) == top or (index+2 == top):
                return cost[index]
            if index+1 > top and index+2 > top:
                return float("inf")     # Force to choose the min of the other option
   
            # Go down both choices -> Memoisation
            hashmap[index] = min(cost[index] + f(index+1),cost[index] + f(index+2))
            return hashmap[index]
        
        # Can start at either index 0 or index 1 
        return min(f(0),f(1))
        



        
        