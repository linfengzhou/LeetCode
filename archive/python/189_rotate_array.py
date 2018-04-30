# first
class Solution(object):

    def rotate(self, nums, k):
        while k > 0:
            num = nums.pop()
            nums.insert(0, num)
            k = k - 1

# second


class Solution(object):

    def rotate(self, nums, k):
        if k > 0:
            nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums)-k]


