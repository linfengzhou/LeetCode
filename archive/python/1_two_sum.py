# my solution
class Solution(object):

    def twoSum(self, nums, target):
        for index, num in enumerate(nums):
            next_target = target - num
            # print 'next_target', next_target
            for index1, num1 in enumerate(nums[index + 1:]):
                # print 'num1',num1
                if num1 == next_target:
                    return [index, index + index1 + 1]


# my better solution
class Solution(object):

    def twoSum(self, nums, target):
        dic = {}
        for index, num in enumerate(nums):
            if (num in dic):
                if (dic[num] != index):
                    return [dic[num], index]
            next_target = target - num
            dic[next_target] = index
