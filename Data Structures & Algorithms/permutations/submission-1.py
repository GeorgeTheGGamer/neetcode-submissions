class Solution:
    def permute(self, nums):
        results = []
    
        def backtrack(path, used):
            if len(path) == len(nums):
                results.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in used:
                    path.append(nums[i])
                    used.add(nums[i])
                    backtrack(path, used)

                    # Remove to move to the next num for the order
                    path.pop()
                    used.remove(nums[i])
        
        backtrack([], set())
        return results
        