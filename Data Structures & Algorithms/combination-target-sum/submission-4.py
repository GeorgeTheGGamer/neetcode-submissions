class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # List of list output is backtracking
        # size of n -> Brute force
        # Have target integer, all unique values to sum to target

        result = []
        def backtrack(index, path, current_sum):
            if current_sum == target:
                result.append(path[:])
                return
            if index == len(nums):
                return
            if current_sum>target:
                return
            

            # Decision 1: Visit this current number
            path.append(nums[index])
            backtrack(index, path, current_sum + nums[index])

            # Decision 2: Skip this number
            path.pop()
            backtrack(index+1, path, current_sum)
        
        backtrack(0,[],0)
        return result
            


            
