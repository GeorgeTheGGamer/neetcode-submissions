class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()     # Inplace sort for two pointers
        result = []

        for i in range(len(nums)):
            # Skip duplicates in i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            current = nums[i]
            while l < r:
                total = current + nums[l] + nums[r]
                if total == target:
                    result.append([current, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Ensure that there are no duplicates
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total < target:
                    l += 1
                elif total > target:
                    r -=1
        
        return result
                
                

        