class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        # Using hashmap to see any that has been visited
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement],i]
            else:
                hashmap[num] = i
            




        
        
        

        