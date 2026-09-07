class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not(self.alphanum(s[l])):
                l +=1
            while r > l and not(self.alphanum(s[r])):
                r -=1
            if s[l].lower() != s[r].lower():
                return False

            l,r = l+1, r-1 # Don't forget to cover the good case 
        
        return True
    
    def alphanum(self, value):
        return ((ord('a') <= ord(value)) and (ord(value) <= ord('z')) or
            (ord('A') <= ord(value)) and (ord(value) <= ord('Z')) or
            (ord('0') <= ord(value)) and (ord(value) <= ord('9')))


            


        
        


        
