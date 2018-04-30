import sys


class Solution(object):

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) == 0:
            return 0
        n = len(A)
        f, total_sum = 0, 0
        for index, val in enumerate(A):
            f += index * val
            total_sum += val
        max_f = - sys.maxsize
        for i in range(n - 1, -1, -1):
            f += total_sum - n * A[i]
            max_f = max(max_f, f)
        return max_f


# if __name__ == '__main__':
#     a = Solution()
#     print(a.maxRotateFunction([4, 3, 2, 6]))
