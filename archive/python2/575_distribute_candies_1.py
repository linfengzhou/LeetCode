class Solution(object):

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        types = set(candies)
        if len(types) >= len(candies) / 2:
            return len(candies) / 2
        else:
            return len(types)
