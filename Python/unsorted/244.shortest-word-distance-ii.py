import sys


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = dict()
        for index, word in enumerate(words):
            self.d[word] = self.d.get(word, []) + [index]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = self.d[word1], self.d[word2]
        i, j, res = 0, 0, sys.maxsize
        while i < len(w1) and j < len(w2):
            res = min(res, abs(w2[j] - w1[i]))
            if w1[i] < w2[j]:
                i += 1
            else:
                j += 1
        return res
        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(words)
        # param_1 = obj.shortest(word1,word2)
