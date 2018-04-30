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
        if not intervals or len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end
        res = 0
        for index, interval in enumerate(intervals):
            if index == 0:
                continue
            if interval.start > end:
                res += end - start
                start = interval.start
                end = interval.end
            else:
                end = max(end, interval.end)
        return res + (end-start)

# if __name__ == '__main__':
#     a = Solution()
#     print(a.merge([Interval(1, 4), Interval(2, 3)]))
