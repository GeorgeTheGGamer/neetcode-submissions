class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        output = 0

        for num in numSet:
            if (num-1) not in numSet:       # Only concerned with the lowest value
                length = 1
                while (num+length) in numSet:
                    length+=1
                output = max(output, length)

        return output

        