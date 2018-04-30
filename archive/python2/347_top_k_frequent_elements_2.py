class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts_dict = {}
        res = []
        res_dict = {}
        for num in nums:
            if num not in counts_dict:
                counts_dict[num] = 1
            else:
                counts_dict[num] += 1

        res_values = list(counts_dict.values())
        sorted_res = sorted(res_values, reverse=True)[:k]

        for value in sorted_res:
            for key in list(counts_dict.keys()):
                if counts_dict[key] == value:
                    res.append(key)
                    counts_dict.pop(key)
        return res
