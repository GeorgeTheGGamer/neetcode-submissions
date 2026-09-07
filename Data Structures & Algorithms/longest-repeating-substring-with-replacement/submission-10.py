class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            # If not valid
            while (r-l+1 - max(count.values())) > k:
                # Shift the left pointer
                count[s[l]] = count[s[l]] - 1
                l += 1
            res = max(res, r-l+1)
        
        return res

        

            

        