class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 2:
            return n
        tab = [0] * (n+1)
        tab[1]=1            # 1 way to get to 1
        tab[2] = 2          # 2 ways to get to 2

        for i in range(3, n+1):         # From index 3 to index n
            tab[i] = tab[i-1] + tab[i-2]
        

        return tab[n]

        