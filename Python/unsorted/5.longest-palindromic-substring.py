class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_left, max_right, max_len = 0, 0, 0
        length = len(s)
        for i in range(1, length * 2):
            if i & 1:
                # aba type
                left = i / 2
                right = left
            else:
                # abba type
                left = i / 2 - 1
                right = left + 1
            while (left >= 0) and (right < length) and (s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left > max_len:
                max_len = right - left
                max_left = left
                max_right = right
        return s[max_left:max_right + 1]
