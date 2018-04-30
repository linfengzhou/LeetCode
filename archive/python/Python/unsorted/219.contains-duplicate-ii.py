class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        nums_dict = dict()

        for index, num in enumerate(nums):
            nums_dict[num] = nums_dict.get(num, []) + [index]
            temp = nums_dict[num]
            if len(temp) > 1 and k >= temp[-1] - temp[-2]:
                return True
        return False
        
# if __name__ == '__main__':
#     a = Solution()
#     print(a.containsNearbyDuplicate([1, 2, 3, 1, 4, 4], 0))
