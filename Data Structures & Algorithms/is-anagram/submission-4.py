class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) or O(nlogn) time complexity wanted
        # Input: String
        # Output: Boolean
        # Anagrams -> HashMap 

        # Make sure the order is the same
        return sorted(s) == sorted(t)



