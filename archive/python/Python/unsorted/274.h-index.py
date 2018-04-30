class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations or len(citations) == 0:
            return 0
        n = len(citations)
        citations.sort()
        max_h = 0
        for h in range(n, 0, -1):
            if citations[n - h] >= h:
                max_h = max(max_h, h)
        return max_h

# if __name__ == '__main__':
#     a = Solution()
#     print(a.hIndex([100]))
