class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Use the goal post
        goal_post = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            # Continue to move the goal post towards the start
            jump = i + nums[i]
            if jump >= goal_post:
                goal_post = i
        
        if goal_post == 0:
            return True
        else:
            return False
        
