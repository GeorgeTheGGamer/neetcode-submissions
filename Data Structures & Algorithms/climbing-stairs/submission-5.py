class Solution:
    def climbStairs(self, n: int) -> int:
        # Climb with either 1 or 2 steps at a time
        # Return the distinct ways to climb the top of the stair case
        # Starting from 0, reach n. take 1 or 2

        hashmap = {}
        def memo(step):
            if step == n:           # When we reach the top, 1
                return 1
            if step > n:
                return 0            # When we exceed the top, 0
            if step in hashmap:
                return hashmap[step]
            else:
                hashmap[step] = memo(step+1) + memo(step+2)
                return hashmap[step]         # Each path we add
        
        return memo(0)

        