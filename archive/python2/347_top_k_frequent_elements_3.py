import heapq


class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        heap = []
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        for key in counts:
            heapq.heappush(heap, (-counts[key], key))
        result = []
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])
        return result
