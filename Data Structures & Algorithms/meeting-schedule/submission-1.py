"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        sched = []
        for i in range(0, len(intervals)):
            interval = intervals[i]
            if sched and interval.start < sched[-1]:
                return False
            sched.append(interval.start)
            sched.append(interval.end)
        return True
