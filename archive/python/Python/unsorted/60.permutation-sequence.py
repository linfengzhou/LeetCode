import math


class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # total = math.factorial(n)
        result = ''
        visited = [False] * n
        # corner case : total == 1?
        current_fac = math.factorial(n)
        k = (k - 1) % current_fac + 1
        k = k - 1
        while n > 0:
            current_fac = current_fac / n
            num = k // current_fac
            k = k % current_fac
            index, count = 0, 0
            while count < num:
                while visited[index]:
                    index += 1
                count += 1
                index += 1
            while visited[index]:
                index += 1
            result += str(index + 1)
            visited[index] = True
            n -= 1
        return result


if __name__ == '__main__':
    a = Solution()
    k = 1
    while k < 10:
        print(a.getPermutation(3, k))
        k += 1
