class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Return the integer that appears twice
        # Use the XOR function of all the numbers and what ever is left is the non duplicate

        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]

        

        return result