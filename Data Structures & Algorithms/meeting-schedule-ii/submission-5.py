"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])  # [0, 5, 15]
        ends = sorted([i.end for i in intervals])      # [10, 20, 40]
        s, e = 0, 0
        max_mtgs, cur_mtgs = 0, 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                cur_mtgs += 1
                max_mtgs = max(max_mtgs, cur_mtgs)
            else:
                e += 1
                cur_mtgs -= 1
        return max_mtgs


        