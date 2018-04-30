class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pa_map = {
            '(': ')',
            ')': '(',
            '[': ']',
            ']': '[',
            '{': '}',
            '}': '{'
        }
        if not s or s in pa_map:
            return False
        if s == "":
            return True
        left, right = 0, len(s) - 1
        while left < right:
            target = s[right]
            if s[left] in pa_map:
                target = pa_map.get(s[right])
            if s[left] != target:
                return False
            left += 1
            right -= 1
        return True
