class Solution:
    def rob(self, nums: List[int]) -> int:
        # Helper Function gets max excluding the start or the end. As you cannot have both
        def maxRob(start, end):
            rob1, rob2 = 0, 0

            if len(nums) == 1:
                return nums[0]

            # Either we exlude index 0 or index n-1
            for i in range(start,end):
                temp = max(rob2, rob1 + nums[i])
                rob1 = rob2
                rob2 = temp
        
            return rob2
        return max(maxRob(0,len(nums)-1), maxRob(1,len(nums)))
        