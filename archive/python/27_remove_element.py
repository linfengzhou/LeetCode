# my solution
class Solution1(object):

    def removeElement(self, nums, val):
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
                j += 1
        return j

# good solution
# just make sure none-filter number at head of the list


class Solution(object):

    def removeElement(self, nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
