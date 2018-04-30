class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        _set = set
        row1 = _set('qwertyuiopQWERTYUIOP')
        row2 = _set('asdfghjklASDFGHJKL')
        row3 = _set('zxcvbnmZXCVBNM')
        row_words = []
        for w in words:
            w_set = _set(w)
            if w_set <= row1 or w_set <= row2 or w_set <= row3:
                row_words.append(w)
        return row_words
