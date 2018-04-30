class Solution(object):

    def reverseVowels(self, s):
        i = 0
        j = len(s) - 1
        v_words = 'aeiouAEIOU'
        s = list(s)
        while i < j:
            if s[i] in v_words and s[j] in v_words:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] in v_words and not(s[j] in v_words):
                j -= 1
            elif s[j] in v_words and not(s[i] in v_words):
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s)
