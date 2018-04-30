class Solution(object):

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1_dict = dict()
        if len(nums1) * len(nums2) == 0:
            return []
        else:
            for num1 in nums1:
                nums1_dict[num1] = 1
            for num2 in nums2:
                if num2 in nums1_dict:
                    res.append(num2)
                    nums1_dict.pop(num2)
            return res
