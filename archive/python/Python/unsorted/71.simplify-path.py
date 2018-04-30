class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []
        paths = path.split('/')
        for sub in paths:
            if sub == '' or sub == '.':
                pass
            elif sub == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(sub)
        return '/' + '/'.join(stack)


# if __name__ == '__main__':
#     a = Solution()
#     print(a.simplifyPath('/home//foo/'))
