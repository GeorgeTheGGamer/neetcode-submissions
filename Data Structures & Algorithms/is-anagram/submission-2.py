class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) or O(nlogn) time complexity wanted
        # Input: String
        # Output: Boolean
        # Anagrams -> Hashmap

        return Counter(s) == Counter(t)