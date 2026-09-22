class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit Manipulation Question
        # Unsigned, return the number of 1 bits in the representation
        # Within 32 bits

        return bin(n).count('1')