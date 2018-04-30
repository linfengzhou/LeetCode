class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1 = nums2[:n]
        elif n == 0:
            pass
        else:
            nums1 = nums1[:m] + nums2[:n]
            nums1.sort()
        return nums1
