class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start date
        # See if overlapping
        # If it is -> Remove the one which ends first

        
        intervals.sort(key = lambda x : x[0])
        count = 0
        end_value = intervals[0][1]

        for i in range(1, len(intervals)):
            # Overlapping
            if intervals[i][0] < end_value:
                # Choose which to remove by least end position
                end_value = min(intervals[i][1], end_value)
                count += 1
            else:
                end_value = intervals[i][1]
        return count



        


