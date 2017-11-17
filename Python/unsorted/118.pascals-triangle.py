class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []

        f = [[0] * i for i in range(1, numRows + 1)]
        for i in range(numRows):
            f[i][0] = 1
            f[i][-1] = 1

        for i in range(2, numRows):
            for j in range(1, i):
                f[i][j] = f[i - 1][j - 1] + f[i - 1][j]

        return f

# if __name__ == '__main__':
#     a = Solution()
#     print(a.generate(2))
