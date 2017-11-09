class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        cur = ''
        stack = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                if cur == '.':
                    pass
                elif cur == '':
                    pass
                elif cur == '..':
                    if len(stack) != 0:
                        stack.pop()
                else:
                    stack.append(cur)
                cur = ''
            else:
                cur += path[i]
            i += 1

        if cur == '.':
            pass
        elif cur == '':
            pass
        elif cur == '..':
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(cur)
        return '/' + '/'.join(stack)

# if __name__ == '__main__':
#     a = Solution()
#     print(a.simplifyPath('/.../'))
