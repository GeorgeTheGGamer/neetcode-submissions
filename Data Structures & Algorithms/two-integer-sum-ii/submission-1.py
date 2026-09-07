class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since O(1) space complexity requirement, no hashmap can be used
        # Assending order so two pointer solution is viable
        l = 0
        r = len(numbers) - 1

        while l < r:
            current = numbers[l] + numbers[r]
            if current > target:
                r-=1
            elif current < target:
                l+=1
            else:
                return [l+1, r+1]       #No need to check order since we know it is assending

        return []
        
                


        