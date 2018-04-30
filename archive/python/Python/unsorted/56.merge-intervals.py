# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        if not intervals:
            return res
        intervals = sorted(intervals, key=lambda x: x.start)
        last_interval = None
        for interval in intervals:
            if not last_interval:
                last_interval = interval
            elif last_interval.end < interval.start:
                res.append(last_interval)
                last_interval = interval
            elif last_interval.end < interval.end:
                last_interval.end = interval.end
        return res + [last_interval]
