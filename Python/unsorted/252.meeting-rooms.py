# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals or len(intervals) == 0:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)
        last_end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < last_end:
                return False
            last_end = intervals[i].end
        return True
