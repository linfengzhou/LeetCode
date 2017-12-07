import heapq


class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        primes = [2, 3, 5]
        Q = []
        inQ = set([])
        for prime in primes:
            Q.append(prime)
        for i in range(1, n):
            res = heapq.heappop(Q)
            for prime in primes:
                new_prime = res * prime
                if new_prime not in inQ:
                    inQ.add(new_prime)
                    heapq.heappush(Q, new_prime)
        return res
