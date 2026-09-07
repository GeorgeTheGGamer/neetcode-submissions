class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:        # Tried this starting number already
                continue
            l,r = i+1, len(nums) - 1
            while l < r:
                current = nums[i] + nums[l] + nums[r]
                if current < target:
                    l+=1
                elif current > target:
                    r-=1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                    
            
        
        return output
                

        

