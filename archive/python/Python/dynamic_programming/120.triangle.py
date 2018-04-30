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
        f = [[None] * n] * n

        # bottom-up

        # initialize
        for i in range(n):
            f[n - 1][i] = triangle[n - 1][i]
            

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):  # maximum of j == i
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]

        return f[0][0]

# if __name__ == '__main__':
#     a = Solution()
#     print(a.minimumTotal([
#         [2],
#         [3, 4],
#         [6, 5, 7],
#         [4, 1, 8, 3]
#     ]
#     ))
