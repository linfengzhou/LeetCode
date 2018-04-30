class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations or len(citations) == 0:
            return 0
        n = len(citations)
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (end - start) // 2
            if citations[mid] >= n - start:
                end = mid
            else:
                start = mid

        if citations[start] >= n - start:
            return n - start
        elif citations[end] >= n - start:
            return n - end
        else:
            return 0


if __name__ == '__main__':
    a = Solution()
    print(a.hIndex([0, 1, 3, 5, 6]))
