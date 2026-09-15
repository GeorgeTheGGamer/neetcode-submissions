class Solution:
    def permute(self, nums):
        results = []
    
        def backtrack(path, used):
            if len(path) == len(nums):
                results.append(path[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path, used)

                    # Remove to move to the next num for the order
                    path.pop()
                    used[i] = False
        
        used = len(nums) * [False]
        backtrack([], used)
        return results
        