"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# intervals = [(0,40),(1,15),(10,20)]
#.                      l     r
# room = 1
# end_time = 40
# if end_time > end time of r
# room = 2


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if end time == start time its not a conflict
        # sort by start time

        # intervals = [(0,40),(5,10),(15,41)]

        # 
        # rooms = [(0, 40), (15,41)]
        # return len(rooms)

        intervals.sort(key=lambda x: x.start)

        # rooms sorted by end time in ascending order
        rooms = []
        for i in range(len(intervals)): #looping through all the intervals
            rooms.append((intervals[i].start, intervals[i].end))
            if rooms[0][1] <= intervals[i].start:
                rooms.remove(rooms[0]) 
            rooms.sort(key=lambda x: x[1]) # resorting rooms based on end time 
            print(rooms)
        return len(rooms)
        


        
        
