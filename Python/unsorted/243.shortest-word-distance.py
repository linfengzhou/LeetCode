import sys


class Solution(object):

    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        source, target = None, None
        res = sys.maxsize
        for index, word in enumerate(words):
            if word == word1:
                source = index
            elif word == word2:
                target = index
            if source is not None and target is not None:
                res = min(res, abs(target - source))
        return min(res, abs(target - source))

# if __name__ == '__main__':
#     a = Solution()
#     print(a.shortestDistance(
#         ["a", "b", "c", "d", "d"],
#         "a", "d"
#     ))
