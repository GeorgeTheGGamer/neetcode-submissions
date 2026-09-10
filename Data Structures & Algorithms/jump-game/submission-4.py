class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Use the goal post
        reached_index = 0
        for i in range(len(nums)):
            if i > reached_index:
                return False
            reached_index = max(reached_index, i+nums[i])
        
        return True
        
