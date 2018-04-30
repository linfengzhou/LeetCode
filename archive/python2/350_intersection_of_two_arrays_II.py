class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n_nums1 = len(nums1)
        n_nums2 = len(nums2)
        if n_nums1 < n_nums2:
            nums1, nums2 = nums2, nums1
        res_nums = {}
        res = []
        for num in nums1:
            if num not in res_nums:
                res_nums[num] = 1
            else:
                res_nums[num] += 1
        for num in nums2:
            if (num in res_nums) and (res_nums[num] > 0):
                res.append(num)
                res_nums[num] -= 1
        return res
