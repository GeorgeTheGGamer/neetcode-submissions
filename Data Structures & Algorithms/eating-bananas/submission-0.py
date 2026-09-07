class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        # Changing pile you eat k bananas

        # Minimum k to seat all bananas within h hours
        l = 1
        r = max(piles)      #[0...max(pile)] Binary Search over possible eating rate

        output = float('inf')
        
        while l <= r:
            hour = 0        # Reset when testing different eat rates
            eatRate = (l+r) // 2
            for pile in piles:                      # Handles case where pile is less than to 1
                hour += math.ceil(pile/eatRate)
                
            # If hours we took greater, then we need a higher eating rate
            if hour > h:
                l = eatRate + 1
            else:
                r = eatRate - 1         # Then continue eating bigger
                output = min(output,eatRate)
        
        return output
                



        

