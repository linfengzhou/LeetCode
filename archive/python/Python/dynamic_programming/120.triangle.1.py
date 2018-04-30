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
        for i in range(n - 2, -1, -1):
            for j in range(0, i + 1):
                triangle[i][j] = triangle[i][j] + min(
                    triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]

# if __name__ == '__main__':
#     a = Solution()
#     print(a.minimumTotal([
#         [2],
#         [3, 4],
#         [6, 5, 7],
#         [4, 1, 8, 3]
#     ]
#     ))
