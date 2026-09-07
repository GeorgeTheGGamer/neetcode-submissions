class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Target sum = 0
        # Two pointer requires to be sorted
        nums.sort()
        output = []
        target = 0

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if l<r and nums[i] == nums[i-1] and i-1 >= 0:        # We are not needing to move the needle here so only an if statement is needed
                continue
            while l < r:
                current = nums[i] + nums[l] + nums[r]
                if current > target:
                    r -= 1
                elif current < target:      # Do not forget the elif statements
                    l += 1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1       
        return output

                

        

