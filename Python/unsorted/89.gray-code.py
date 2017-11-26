class Solution(object):

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i ^ (i // 2) for i in range(0, 1 << n)]

# if __name__ == '__main__':
#     a = Solution()
#     print(a.grayCode(0))

# class Solution(object):
#     def grayCode(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         res = []
#         if n == 0 :
#             return [0]
#         for i in range(2**n):  # 1 << n
#             res.append(i ^ (i//2))
#         return res
#
