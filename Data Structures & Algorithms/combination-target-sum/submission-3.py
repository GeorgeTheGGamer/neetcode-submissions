class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, path, current):
            if current == target:
                result.append(path[:])
                return
            if current > target:
                return
            if index == len(nums):
                return
            
            # Decision 1: Stay on current number
            path.append(nums[index])
            backtrack(index, path, current + nums[index])
            path.pop()

            # Decision 2: Move to the next value
            backtrack(index+1, path, current)
        
        backtrack(0, [], 0)
        return result