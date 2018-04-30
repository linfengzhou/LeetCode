from collections import deque


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
        if endWord not in words:
            return 0
        queue, hashset = deque([[beginWord, 1]]), set([])

        while len(queue) != 0:
            word_info = queue.popleft()
            word = word_info[0]
            cur_len = word_info[1]
            if word == endWord:
                return cur_len
            for i in range(len(word)):
                part1, part2 = word[:i], word[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] != j:
                        next_word = part1 + j + part2
                        if next_word in words and next_word not in hashset:
                            queue.append([next_word, cur_len + 1])
                            hashset.add(next_word)
        return 0
