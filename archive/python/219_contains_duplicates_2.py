# my solution Time Limit Exceeded
class Solution(object):

    def containsNearbyDuplicate(self, nums, k):

        if len(nums) < 2:
            return False
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                return True
            else:
                return False
        for index, num in enumerate(nums):
            if num in nums[index + 1:]:
                for index1, num1 in enumerate(nums[index + 1:]):
                    if num == num1:
                        if index1 + 1 <= k:
                            return True
        return False

# good solution


class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                diff = index - dic[num]
                if diff <= k:
                    return True
            dic[num] = index
        return False

# need more good solution
