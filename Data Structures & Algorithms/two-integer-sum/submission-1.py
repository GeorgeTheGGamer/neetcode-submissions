class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i,num in enumerate(nums):
            # We have the current num index, we need to see if the difference is already within the hashmap
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[num] = i
            




        
        
        

        