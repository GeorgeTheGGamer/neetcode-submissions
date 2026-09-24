class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Remove overlapping intervals -> Choose the one with the smallest end point

        intervals.sort(key = lambda x : x[0])
        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                count+=1
                prev_end = min(end, prev_end)
            else:
                prev_end = end
        

        return count