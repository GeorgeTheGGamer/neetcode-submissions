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

            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1, path)
        
        backtrack(0,[])
        return results

        