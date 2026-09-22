class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Return integer that appears once

        # O(1) extra space -> Only variables to hold it 
        # Must use XOR to cancel out all the duplicates to be 0, then the result is the one that is different
        res = 0
        for n in nums:
            res = res ^ n
        return res
        