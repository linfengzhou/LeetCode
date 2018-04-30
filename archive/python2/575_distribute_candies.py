class Solution(object):

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candies_map = dict()
        n_candies = len(candies)
        for candi in candies:
            if candi not in candies_map:
                candies_map[candi] = 1
            else:
                candies_map[candi] += 1
        candies_list = sorted(candies_map, key=candies_map.get)
        n_candies_kinds = len(candies_list)
        i = 0
        res = 0
        while i < n_candies / 2:
            if i < n_candies_kinds:
                res += 1
            else:
                return n_candies_kinds
            i += 1
        return res
