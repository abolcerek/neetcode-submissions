"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start) #sorting the times based on the start time

        for i in range(1, len(intervals)): #for every time interval in intervals
            i1 = intervals[i-1] #the first interval is the previous interval
            i2 = intervals[i] #the second interval is the next interval
            if i1.end > i2.start: #if the end time of the first interval is greater than the start time of the next interval
                return False #return false, since we know that is overlapped
        return True #return true outside the loop because if it went through the loop and didnt return false we know that there wasnt an overlap