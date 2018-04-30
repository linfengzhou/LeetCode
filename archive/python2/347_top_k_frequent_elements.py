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
        for i in range(k):
            neg_i = str(i)
            res_dict[neg_i] = 0

        def check_res_dict(res_dict):
            res_min = None
            res_min_value = None
            for key in res_dict:
                if res_min is None:
                    res_min = key
                    res_min_value = res_dict[key]
                else:
                    if res_min_value > res_dict[key]:
                        res_min = key
                        res_min_value = res_dict[key]
            return res_min, res_min_value

        res_min, res_min_value = check_res_dict(res_dict)
        for num in counts_dict:
            if counts_dict[num] > res_min_value:
                res_dict[num] = counts_dict[num]
                res_dict.pop(res_min)
                res_min, res_min_value = check_res_dict(res_dict)
        res = list(res_dict.keys())
        return res
