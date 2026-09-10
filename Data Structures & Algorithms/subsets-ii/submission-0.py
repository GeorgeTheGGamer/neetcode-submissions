class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        def backtrack(index, path):
            if index == len(nums):
                results.append(path[::])
                return
                
            # Explore this path
            path.append(nums[index])
            backtrack(index+1,path)

            # Backtrack and explore this path
            path.pop()
            
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1, path)
        
        backtrack(0,[])
        return results
        

