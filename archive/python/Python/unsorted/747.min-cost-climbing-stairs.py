import sys


class Solution(object):

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        # define f[n]: the min cost before node n
        # for [10,15,20]
        # f[0] => 0 f[1] = 0 f[2] = 10 f[3] = 10 f[4] = 15
        n = len(cost)
        f = [sys.maxsize] * (n + 1)
        f[0] = 0
        f[1] = 0
        for i in range(2, n + 1):
            f[i] = min(f[i - 1] + cost[i - 1], f[i - 2] + cost[i - 2])
        return f[n]

# if __name__ == '__main__':
#     a = Solution()
#     print(a.minCostClimbingStairs([10, 15, 20]
#                                   ))
