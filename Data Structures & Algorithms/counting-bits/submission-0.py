class Solution:
    def countBits(self, n: int) -> List[int]:
        # Count the number of 1's in every single number 
        result = []
        for i in range(n+1):
            count = 0
            while i:
                count += i%2
                i = i >> 1
            result.append(count)
        

        return result
                
        