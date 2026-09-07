class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Create hashmaps for each string
        hashmap_s, hashmap_t = dict(), dict()

        # If they were anagrams then they would be the same
        if len(s) != len(t):
            return False
        
        # The hashmaps have the key as the string and the counts here
        # get allows for finding a value even if it is not there
        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i],0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i],0) 

        return hashmap_s == hashmap_t




