class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Return the integer that appears twice
        # Use the XOR function of all the numbers and what ever is left is the non duplicate

        result = 0
        for num in nums:
            result = result ^ num

        

        return result