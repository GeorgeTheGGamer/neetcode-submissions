class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # n <= 20 + combination sum = Backtracking
        results = []

        def backtrack(index, path, current):

            # Base case where is equal to the target
            if current == target:
                results.append(path[:])
                return

            # Base case where we reach the end of nums
            if index == len(nums):
                return
            
            # Base case where target is exceeded
            if current > target:
                return

            # Decison 1: Stay on the same number
            path.append(nums[index])
            backtrack(index, path, current + nums[index])
            path.pop()


            # Decision 2: Or skip to the next number
            backtrack(index+1, path, current)

        backtrack(0, [], 0)
        return results
    




