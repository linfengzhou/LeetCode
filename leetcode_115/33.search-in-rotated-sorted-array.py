class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # [1, 2, 3, 4, 5, 6]
        # [4, 5, 6, 1, 2, 3]
        if not nums or len(nums) == 1:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if target <= nums[end]:
                if target > nums[mid]:
                    start = mid
                elif nums[mid] > nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[mid] > target:
                    end = mid
                elif nums[mid] < nums[end]:
                    end = mid
                else:
                    start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
if __name__ == '__main__':
    a = Solution()
    print(a.search([4, 5, 6, 1, 2, 3], 4))
