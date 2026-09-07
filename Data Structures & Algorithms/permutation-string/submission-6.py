class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Permutations -> Sliding Window
        # Fixed window as a permutation will always be the length of s1
        
        l = 0
        r = len(s1)

        # Count of letters in s1
        count = [0] * 26
        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            count[index] +=1

        while r<=len(s2):
            currentCount = [0] * 26
            
            for i in range(l,r):
                index = ord(s2[i]) - ord('a')
                currentCount[index] +=1
            print(currentCount)

            if currentCount == count:
                return True
            else:
                l += 1
                r += 1
            
        return False