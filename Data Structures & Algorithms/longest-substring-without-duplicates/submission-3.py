class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Longest CONTIGUOUS substring -> Sliding Window
        # O(n) approach

        seen = set()
        result = 0
        l=0

        # We want to add to the set
        # We want to add to the substring
        # We want to keep the max length of substring

        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                result = max(result, len(seen))               
            else:
                seen.add(s[r])
                result = max(result, len(seen))



        return result
 