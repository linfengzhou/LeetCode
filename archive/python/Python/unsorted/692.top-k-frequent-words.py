class Solution(object):

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words_dict = dict()
        for word in words:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        words_list = [(v, i) for (i, v) in words_dict.items()]
        # print(words_list)
        words_list = sorted(
            words_list, key=lambda x: (-1 * x[0], x[1]), reverse=False)
        # print(words_list)
        res = []
        for i in range(k):
            res.append(words_list[i][1])
        return res
# if __name__ == '__main__':
#     a = Solution()
#     print(a.topKFrequent(["the", "day", "is", "sunny",
#                           "the", "the", "the", "sunny", "is", "is"], 2))
