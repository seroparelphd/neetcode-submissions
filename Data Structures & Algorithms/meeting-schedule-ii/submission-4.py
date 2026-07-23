"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        sched = []
        max_rooms = 0
        for interval in intervals:
            if sched and sched[0] <= interval.start:
                heapq.heappop(sched)
            heapq.heappush(sched, interval.end)
            max_rooms = max(max_rooms, len(sched))
        return max_rooms  # len(sched)