class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        if nums == []:
            return [-1, -1]
        # search for left bound
        res = []
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            res.append(start)
        elif nums[end] == target:
            res.append(end)
        else:
            return [-1, -1]

        start, end = res[0], len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                start = mid
            else:
            	end = mid
        if nums[end] == target:
            res.append(end)
        else:
            res.append(start)
    	return res