import math


class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return ''
        total_fact = math.factorial(n)
        result = []
        visited = [False] * n
        k = (k - 1) % total_fact + 1
        k -= 1
        for i in range(n):
            total_fact = total_fact / (n - i)
            num = k // total_fact
            k = k % total_fact
            for j in range(n):
                if not visited[j]:
                    if num == 0:
                        result.append(str(j + 1))
                        visited[j] = True
                        break
                    num -= 1
        return ''.join(result)
