import sys


class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if not triangle or len(triangle) == 0:
            return -1
        if not triangle[0] or len(triangle[0]) == 0:
            return -1

        n = len(triangle)
        f = [[0] * n for i in range(n)]

        # init
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            f[i][0] = triangle[i][0] + f[i - 1][0]
            f[i][i] = triangle[i][i] + f[i - 1][i - 1]

        for i in range(1, n):
            for j in range(1, i):
                f[i][j] = triangle[i][j] + \
                    min(f[i - 1][j - 1], f[i - 1][j])

        best = f[n - 1][0]
        for i in range(1, n):
            if f[n - 1][i] < best:
                best = f[n - 1][i]

        return best

# if __name__ == '__main__':
#     a = Solution()
#     print(a.minimumTotal([
#         [2],
#         [3, 4],
#         [6, 5, 7],
#         [4, 1, 8, 3]
#     ]
#     ))
