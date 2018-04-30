class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = set([])
        for word in wordList:
            words.add(word)
        length = 2
        front, back = set([beginWord]), set([endWord])
        if beginWord in words:
            words.remove(beginWord)
        if endWord not in words:
            return 0
        while front:
            # generate all valid transformations
            total_words = set([])
            for j in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(len(beginWord)):
                    for word in front:
                        total_words.add(word[:i] + j + word[i + 1:])
            front = words & total_words
            if front & back:
                # there are common elements in front and back, done
                return length
            length += 1
            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in
                # generating nextSet)
                front, back = back, front
            # remove transformations from wordDict to avoid cycle
            words -= front
        return 0
