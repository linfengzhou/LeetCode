class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations or len(citations) == 0:
            return 0

        n = len(citations)
        cite_dict = dict((i, 0) for i in range(n + 1))
        for cite in citations:
            if cite >= n:
                cite_dict[n] += 1
            else:
                cite_dict[cite] += 1
        paper = 0
        for i in range(n, -1, -1):
            paper += cite_dict[i]
            if paper >= i:
                return i
# if __name__ == '__main__':
#     a = Solution()
#     print(a.hIndex([100]))
