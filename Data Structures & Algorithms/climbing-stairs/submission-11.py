class Solution:
    def climbStairs(self, n: int) -> int:

        # Tabulation: Each cell holds number of ways to get to that cell
        # Optimisation of space
        if n < 2:
            return n
        prev=1            # 1 way to get to 1
        curr = 2          # 2 ways to get to 2

        for i in range(3, n+1):         # From index 3 to index n
            prev, curr = curr, curr+prev
        

        return curr

        