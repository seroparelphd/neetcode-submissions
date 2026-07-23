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
        for interval in intervals:
            if sched and sched[0] <= interval.start:
                heapq.heappop(sched)
                # print(f"heapq.heappop(sched): {heapq.heappop(sched)}")
                # print(f"heappop -> {sched}")
            heapq.heappush(sched, interval.end)
            # print(f"heapq.heappush(sched, interval.end): {heapq.heappush(sched, interval.end)}")
            # print(f"heappush -> {sched}")
        return len(sched)