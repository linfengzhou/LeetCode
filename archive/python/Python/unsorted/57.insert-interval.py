# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals or len(intervals) == 0:
            return [newInterval]
        res = []
        start, end = intervals[0].start, intervals[0].end
        for index, interval in enumerate(intervals):
            if interval.end < newInterval.start:
                res.append(interval)
            elif interval.start > newInterval.end:
                res.append(newInterval)
                newInterval = None
                res += intervals[index:]
                break
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
        if newInterval:
            res += [newInterval]
        return res
