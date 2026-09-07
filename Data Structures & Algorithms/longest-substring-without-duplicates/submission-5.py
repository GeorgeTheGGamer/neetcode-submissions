class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Longest CONTIGUOUS substring -> Sliding Window
        # O(n) approach

        seen = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l +=1
            seen.add(s[r])
            result = max(result, len(seen))

        return result
 