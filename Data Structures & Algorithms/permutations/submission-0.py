class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        seen = set()
        def backtrack(path,seen):
            if len(path) == len(nums):
                results.append(path[:])
                return

            
            for i in range(len(nums)):
                if nums[i] not in seen:
                    path.append(nums[i])
                    seen.add(nums[i])
                    backtrack(path, seen)
                    path.pop()
                    seen.remove(nums[i])


            
        backtrack([], seen)
        return results
            

        