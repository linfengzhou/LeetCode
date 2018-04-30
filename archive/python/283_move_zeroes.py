# my solution O(n^2)
class Solution1(object):

    def moveZeroes(self, nums):
        n_nums = len(nums)
        for i in range(n_nums):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)


# good solution O(n)
# make sure every head elements are none zero
class Solution(object):

    def moveZeroes(self, nums):
        j = 0
        for i, c in enumerate(nums):
            if c != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            print nums
