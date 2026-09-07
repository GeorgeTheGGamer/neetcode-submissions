class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency of nums -> hashmap
        hashmap = {}

        # Now have the counts of numbers
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)
        
        # Sort the top counts
        array = []
        for num, count in hashmap.items():
            array.append([count,num])
        array.sort() # Sort in assending order

        # Retrieve the top k counts
        result = []
        for i in range(k):
            result.append(array.pop()[1]) # We are wanting the list of numbers not their counts
        return result