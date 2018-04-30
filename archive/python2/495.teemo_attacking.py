class Solution(object):

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total_duration = 0
        last_po = None
        if len(timeSeries) == 0:
            return 0
        else:
            for time in timeSeries:
                if last_po is None:
                    last_po = time
                if time <= last_po + duration:
                    total_duration = total_duration + (time - last_po)
                    last_po = time
                else:
                    total_duration += duration
                    last_po = time
            return total_duration + duration
