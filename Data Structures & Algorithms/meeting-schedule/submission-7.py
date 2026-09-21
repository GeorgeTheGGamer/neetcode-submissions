"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort the intervals -> O(nlgn)
        # Then do one pass over comparing start and end

        intervals.sort(key = lambda x : x.start)

        for i in range(len(intervals)-1):
            if intervals[i+1].start < intervals[i].end:
                return False
        
        return True

