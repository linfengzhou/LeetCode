class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if s[i] == ')' and item != '(':
                    return False
                elif s[i] == ']' and item != '[':
                    return False
                elif s[i] == '}' and item != '{':
                    return False
        return len(stack) == 0
