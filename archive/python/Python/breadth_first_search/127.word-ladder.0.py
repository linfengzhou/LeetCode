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
        queue = deque([[beginWord, 1]])
        while len(queue) != 0:
            curr = queue.popleft()
            curr_word = curr[0]
            step = curr[1]
            for i in range(len(curr_word)):
                part1 = curr_word[:i]
                part2 = curr_word[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if curr_word[i] != j:
                        next_word = part1 + j + part2
                        if next_word == endWord:
                            return step + 1
                        if next_word in words:
                            words.remove(next_word)
                            queue.append([next_word, step + 1])
        return 0
