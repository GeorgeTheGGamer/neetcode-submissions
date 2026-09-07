class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Longest substring -> Sliding window 
        # O(n)
        # Intead of unique values, they must be the same
        # So have the counts
        # if the window length - max values of hashmap is greater that while then increment and take away from that specific count 

        count = {}
        result = 0
        l = 0

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r-l+1)

        return result         

            

        