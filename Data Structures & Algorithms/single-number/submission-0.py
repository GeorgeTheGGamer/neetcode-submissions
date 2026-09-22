class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Return integer that appears once

        # O(1) extra space -> Only variables to hold it 
        res = 0
        for n in nums:
            res = res ^ n
        return res
        