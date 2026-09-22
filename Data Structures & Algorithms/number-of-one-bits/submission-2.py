class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit Manipulation Question
        # Unsigned, return the number of 1 bits in the representation
        # Within 32 bits

        res = 0

        while n != 0:
            res += n % 2
            n = n >> 1

        return res