class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # To return all possible subsets, we must use the backtracking algorithm
        result = []

        def backtrack(index, path):
            if index == len(nums):
                result.append(path[:])          # Make a copy due to storing as pointers vs new memory
                return
            

            # Decision 1: Include nums[index]
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()                  # No for the case where did not take that num

            # Decision 2: 
            backtrack(index+1,path)
        
        backtrack(0,[])
        return result
        
        