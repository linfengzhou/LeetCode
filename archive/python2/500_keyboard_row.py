class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_dict = {1: 'qwertyuiop',
                    2: 'asdfghjkl',
                    3: 'zxcvbnm'}
        res = []
        for word in words:
            word_row = 0
            check_con = True
            for row in row_dict:
                if word[0].lower() in row_dict[row]:
                    word_row = row_dict[row]
            for char in word:
                if char.lower() not in word_row:
                    check_con = False
                    continue
            if check_con:
                res.append(word)

        return res
