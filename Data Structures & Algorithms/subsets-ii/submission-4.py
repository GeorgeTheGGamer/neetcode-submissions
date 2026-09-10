class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        def backtrack(index, path):
            if index == len(nums):
                results.append(path[:])
                return
            
            #First we check the elements
            path.append(nums[index])
            # Keep recursively calling until the base condition
            backtrack(index+1, path)
            # Now start backtracking
            path.pop()

        
            # If we choose NOT to include nums[index], skip all remaining copies 
            # of this same value to avoid generating duplicate subsets
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1  # Fast-forward to the last duplicate instance
            
            # Move to the next unique element (index + 1) for the exclude branch
            backtrack(index + 1, path)
        
        backtrack(0,[])
        return results

        