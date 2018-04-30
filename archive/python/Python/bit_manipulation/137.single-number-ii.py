class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = 0, 0, 0
        for i in nums:
            # update two: if i in one, update two
            two = two | (one & i)
            # if show twice, should be zero in one
            one = one ^ i
            # if one and two both include, should be three
            three = one & two
            # update one and tow, make sure not include num which are in three
            one = one & (~three)
            two = two & (~three)
        return one
