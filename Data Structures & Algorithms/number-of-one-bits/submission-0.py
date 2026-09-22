class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit Manipulation Question
        # Unsigned, return the number of 1 bits in the representation
        # Within 32 bits

        binary = bin(n)[2:]
        count = 0
        for number in binary:
            if number == "1":
                count += 1
        

        return count