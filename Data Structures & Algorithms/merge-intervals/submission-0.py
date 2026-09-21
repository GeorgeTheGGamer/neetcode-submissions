class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Intervals question -> O(nlgn)
        # Return the non-overlapping

        # [1,2] [2,3] are overlapping 

        # This sorts by the start values
        intervals.sort(key = lambda x : x[0])
        stack = []
        output = []

        # Add to the stack from largest to smallest
        for i in range(len(intervals)-1, -1, -1):
            stack.append(intervals[i])

        while len(stack) > 1:
            first = stack.pop()
            second = stack.pop()
            # Keep adding the new merged interval
            if second[0] <= first[1]:
                stack.append([min(first[0], second[0]),max(first[1],second[1])])
            else:
                output.append(first)
                stack.append(second)
        
        output.append(stack.pop())
        return output



        