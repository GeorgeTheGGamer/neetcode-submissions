class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Trying out using a hashmap 

        hashmap = {}
        for i,num in enumerate(numbers):
            current = target - num
            if current in hashmap:
                if (i < hashmap[current]):
                    return [i + 1, hashmap[current] + 1]
                else:
                    return [hashmap[current] + 1,i + 1]
            else:
                hashmap[num] = i
        
        return []


        
                


        