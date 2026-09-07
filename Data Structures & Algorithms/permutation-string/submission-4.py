class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Permutations -> Sliding Window
        # Fixed window as a permutation will always be the length of s1

        #O(26n) time complexity 
        
        l = 0
        r = len(s1)   
        count = {}     

        # Count of letters in s1
        for i in range(r):
            count[s1[i]]  =  1 + count.get(s1[i] , 0)

        while r<=len(s2):
            
            currentCount = {}          
            for i in range(l,r):
                currentCount[s2[i]] = 1 + currentCount.get(s2[i],0)

            if currentCount == count:
                return True
            else:
                l += 1
                r += 1
            
        return False

            
            






            



        